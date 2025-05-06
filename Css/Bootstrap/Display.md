* `d-{breakpoint}-{value}`
    * `{breakpoint}`: xs, sm, md, lg, xl, xxl
    * `{value}`: none, inline, block, inline-block, flex, grid, table, table-cell, و غیره

<div style="direction: rtl">

| مقدار‌بوت‌استرپ  | معادل CSS                | توضیح کوتاه                               |
|------------------|--------------------------|-------------------------------------------|
| `d-none`         | `display: none;`         | المان هیچ موقع نمایان نیست                |
| `d-inline`       | `display: inline;`       | المان به صورت خطی نمایش داده شود          |
| `d-block`        | `display: block;`        | المان به صورت بلوکی نمایش داده شود        |
| `d-inline-block` | `display: inline-block;` | المان به صورت inline-block نمایش داده شود |
| `d-flex`         | `display: flex;`         | استفاده از Flexbox برای layout            |
| `d-grid`         | `display: grid;`         | استفاده از CSS Grid برای layout           |

| کلاس           | معنی / رفتار                        | نمایان در چه اندازه‌ها؟ | پنهان در چه اندازه‌ها؟  |
|----------------|-------------------------------------|-------------------------|-------------------------|
| `d-none`       | المان هیچ موقع نمایان نیست          | —                       | xs, sm, md, lg, xl, xxl |
| `d-inline`     | المان به صورت inline نمایان است     | xs                      | —                       |
| `d-block`      | المان به صورت block نمایان است      | xs                      | —                       |
| `d-flex`       | المان با display: flex نمایان است   | xs                      | —                       |
| `d-grid`       | المان با display: grid نمایان است   | xs                      | —                       |
| `d-sm-none`    | المان فقط در sm و بالاتر پنهان است  | xs                      | sm, md, lg, xl, xxl     |
| `d-sm-inline`  | المان فقط در sm و بالاتر inline است | sm, md, lg, xl, xxl     | xs                      |
| `d-sm-block`   | المان فقط در sm و بالاتر block است  | sm, md, lg, xl, xxl     | xs                      |
| `d-sm-flex`    | المان فقط در sm و بالاتر flex است   | sm, md, lg, xl, xxl     | xs                      |
| `d-sm-grid`    | المان فقط در sm و بالاتر grid است   | sm, md, lg, xl, xxl     | xs                      |
| `d-md-none`    | المان فقط در md و بالاتر پنهان است  | xs, sm                  | md, lg, xl, xxl         |
| `d-md-inline`  | المان فقط در md و بالاتر inline است | md, lg, xl, xxl         | xs, sm                  |
| `d-md-block`   | المان فقط در md و بالاتر block است  | md, lg, xl, xxl         | xs, sm                  |
| `d-md-flex`    | المان فقط در md و بالاتر flex است   | md, lg, xl, xxl         | xs, sm                  |
| `d-md-grid`    | المان فقط در md و بالاتر grid است   | md, lg, xl, xxl         | xs, sm                  |
| `d-lg-none`    | المان فقط در lg و بالاتر پنهان است  | xs, sm, md              | lg, xl, xxl             |
| `d-lg-inline`  | المان فقط در lg و بالاتر inline است | lg, xl, xxl             | xs, sm, md              |
| `d-lg-block`   | المان فقط در lg و بالاتر block است  | lg, xl, xxl             | xs, sm, md              |
| `d-lg-flex`    | المان فقط در lg و بالاتر flex است   | lg, xl, xxl             | xs, sm, md              |
| `d-lg-grid`    | المان فقط در lg و بالاتر grid است   | lg, xl, xxl             | xs, sm, md              |
| `d-xl-none`    | المان فقط در xl و بالاتر پنهان است  | xs, sm, md, lg          | xl, xxl                 |
| `d-xl-inline`  | المان فقط در xl و بالاتر inline است | xl, xxl                 | xs, sm, md, lg          |
| `d-xl-block`   | المان فقط در xl و بالاتر block است  | xl, xxl                 | xs, sm, md, lg          |
| `d-xl-flex`    | المان فقط در xl و بالاتر flex است   | xl, xxl                 | xs, sm, md, lg          |
| `d-xl-grid`    | المان فقط در xl و بالاتر grid است   | xl, xxl                 | xs, sm, md, lg          |
| `d-xxl-none`   | المان فقط در xxl پنهان است          | xs, sm, md, lg, xl      | xxl                     |
| `d-xxl-inline` | المان فقط در xxl inline است         | xxl                     | xs, sm, md, lg, xl      |
| `d-xxl-block`  | المان فقط در xxl block است          | xxl                     | xs, sm, md, lg, xl      |
| `d-xxl-flex`   | المان فقط در xxl flex است           | xxl                     | xs, sm, md, lg, xl      |
| `d-xxl-grid`   | المان فقط در xxl grid است           | xxl                     | xs, sm, md, lg, xl      |

مثال:

* d-sm-flex: المان فقط در اندازه‌های sm, md, lg, xl, xxl با display: flex نمایان می‌شود و در xs پنهان است
* d-lg-none: المان فقط در اندازه‌های lg, xl, xxl پنهان می‌شود و در xs, sm, md نمایان است.
* d-none:المان هیچ موقع نمایان نیست — در هیچ اندازه‌ای (xs, sm, md, lg, xl, xxl) دیده نمی‌شود.
* d-inline:المان فقط در اندازه xs به صورت inline نمایان است و در بقیه اندازه‌ها همیشه inline باقی می‌ماند (در صورت عدم وجود کلاس دیگر).
* d-sm-none:المان فقط در اندازه‌های sm, md, lg, xl, xxl پنهان می‌شود و در xs نمایان است.
* d-md-flex:المان فقط در اندازه‌های md, lg, xl, xxl با display: flex نمایان می‌شود و در xs, sm به صورت پیش‌فرض نمایان یا مطابق کلاس دیگری است.
* d-lg-block:المان فقط در اندازه‌های lg, xl, xxl با display: block نمایان می‌شود و در xs, sm, md به صورت پیش‌فرض نمایان یا مطابق کلاس دیگری است.
* d-xl-grid:المان فقط در اندازه‌های xl, xxl با display: grid نمایان می‌شود و در xs, sm, md, lg به صورت پیش‌فرض نمایان یا مطابق کلاس دیگری است.
* d-xxl-none:المان فقط در اندازه xxl پنهان می‌شود و در تمام اندازه‌های دیگر (xs, sm, md, lg, xl) نمایان است.
* d-md-inline:المان فقط در اندازه‌های md, lg, xl, xxl به صورت inline نمایان می‌شود و در xs, sm پنهان است (یا مطابق کلاس قبلی عمل می‌کند).

</div>
