#OS codename (i.e. Focal Fossa)
distroCodeName=$(lsb_release -c | awk '{print $2}')


#OS ID (i.e. Ubuntu)
distroName=$(lsb_release -i | awk '{print $3}')


#OS Release (i.e. 20.04.2)
distroVersion=$(lsb_release -r | awk '{print $2}')


#OS kernel name
kernelName=$(uname -s)


#OS kernel release (i.e. 4.4.0-140-generic)
kernelRelease=$(uname -r)