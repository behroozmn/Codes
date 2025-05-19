for disk in $disks; do
        if [[ ! $disk =~ ^(mirror|cache|log|spare|raid) ]]; then
            if [ ! -e "$disk" ]; then
                log_msg "WARNING" "Disk $disk not found in system"
                log_dualsp_action "-" "$parentid" "Check disk $disk" "Disk not found in system" 1
                continue
            fi

            # Start disk rescan in the background
            {
                wcl=$(ls -lh "$disk"* 2>/dev/null | grep -c "part")
                if [ "$wcl" -ne 2 ]; then
                    part=$(readlink -f "$disk")
                    log_msg "INFO" "Running fdisk on $part"

                    # Run fdisk command
                    output=$(printf q | /sbin/fdisk "$part" 2>&1)

                    # Log the action synchronously to avoid nested background jobs
                    log_dualsp_action "-" "$parentid" "Running fdisk for $disk" "Done fdisk for $disk, $output" 0 "no"
                else
                    log_msg "INFO" "Disk $disk already has partitions"
                fi
            } &

            ((job_count++))

            # Limit the number of parallel jobs
            if [ "$job_count" -ge "$max_parallel_jobs" ]; then
                wait -n  # Wait for any background job to finish
                ((job_count--))
            fi
        fi
