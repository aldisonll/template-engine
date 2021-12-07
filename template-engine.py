import re
from typing import List, Tuple

# simple for loop template
example_template = '''
<h1>For loops</h1>
<ol>
{%for i in range(5)%}
    <li>{{i}}</li>
{%endloop%}
</ol>    
'''

# loop using enumerate
example_template_2 = '''
<h1>For loops</h1>
<ol>
{%for i, x in enumerate(range(5))%}
    <li>{{i}} - {{x}}</li>
{%endloop%}
</ol>    
'''

# using multiple loops
example_template_3 = '''
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
'''

# loop through a dictionary
example_template_4 = '''
<h1>For loops</h1>
{%for name in ["name_1", "name_2"]%}
    <h3>Hello, {{ name }}</h3>
{%endloop%}
'''

loop = r'{%for.*?{%endloop%}'
variable = r'{{.*}}'
loop_value = r'for '

loop_starts_with = '{%for '
loop_ends_with = '{%endloop%}'

remove_template_from_loop = r'{%for(.*?){%endloop%}'

def find_template_loops(template: str) -> List[str]:
    loops: List[str] = re.findall(loop, template, re.DOTALL)
    return loops

def create_dumb_loop(template_loop: str) -> str:
    dumb_loop = re.findall(remove_template_from_loop, template_loop, re.DOTALL)[0].replace('%}', ':')
    return 'for' + dumb_loop

def loop_parser(dumb_loop: str) -> Tuple[str, str]:
    loop_header_ends = dumb_loop.find('\n')
    for_loop_header = dumb_loop[0: loop_header_ends - 0x1]
    vars = dumb_loop[loop_header_ends:]
    return for_loop_header, vars

def execute(for_loop_header: str, vars: str) -> str:
    vars = vars[0x1:].replace('\n', '<br>').replace('{{', '{').replace('}}', '}')
    code = f'''''.join(f'{vars}' {for_loop_header})'''
    return eval(code)

def generate_template(template: str) -> str:
    new_template = template
    loops = find_template_loops(template)
    for loop in loops:
        dumb_loop = create_dumb_loop(loop)
        for_loop_header, vars = loop_parser(dumb_loop)
        loop_template_result = execute(for_loop_header, vars)
        new_template = new_template.replace(loop, loop_template_result)
    return new_template


if "__main__" == __name__:
    print('Example:', example_template_3)
    template = generate_template(example_template_3)
    print('Output:', template)
