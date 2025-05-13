<center>

![ruleset](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_syntax/Syntax/ruleset.png)
<br>
![_declaration](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_syntax/Syntax/css_syntax_-_declaration.png)
<br>
![](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_syntax/Syntax/css_syntax_-_statements_venn_diag.png)
![]()
![]()

</center>

* دو نوع statement داریم
    * نوع Rulesets :مجموعه‌ای از declaration های CSS که توسط Selectorها تخصیص پیدا می‌کنند
        * نوع At-rules: مواردی که با علامت @ آغاز می‌شوند.

# 2.At-rules

* شامل موارد زیر می‌شود
    * @charset
    * @color-profile
    * @container
    * @counter-style
    * @font-face
    * @font-feature-values
    * @font-palette-values
    * @keyframes
    * @layer
    * @media
    * @namespace
    * @page
    * @position-try
    * @property
    * @scope
    * @starting-style
    * @supports
    * @view-transition

## @import

```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,700;1,900&display=swap');

html {
    font-family: 'Roboto', sans-serif;
}
```


