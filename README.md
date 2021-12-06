## Simple Template Engine

### Example
```bash
'''
<h1>For loops</h1>
<ol>
{%for i in range(5)%}
    <li>{{i}}</li>
{%endloop%}
</ol> 
<ol>
{%for i in range(5)%}
    <li>{{ i }} x 7 = {{i * 7}}</li>
{%endloop%}
</ol> 
''''
```
### Output
```html
<h1>For loops</h1>
<ol>
    <li>0</li><br>
    <li>1</li><br>
    <li>2</li><br>
    <li>3</li><br>
    <li>4</li><br>
</ol>
<ol>
    <li>0 x 7 = 0</li><br>
    <li>1 x 7 = 7</li><br>
    <li>2 x 7 = 14</li><br>
    <li>3 x 7 = 21</li><br>
    <li>4 x 7 = 28</li><br>
</ol>

```
