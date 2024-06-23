filesystem = {
    'path': 'C:',
    'content': [
        {
            'path': 'documents',
            'content': [
                {
                    'path': 'pictures',
                    'content': [
                        {
                            'path': 'me.png',
                            'content': [],
                        },
                        {
                            'path': 'keks.png',
                            'content': [],
                        }
                    ]
                }
            ]
        }
    ]
}


def print_recursively(filesystem):
    def traverse(content):
        for item in content:
            print(item['path'])
            if item['content']:
                traverse(item['content'])

    print(filesystem['path'])
    traverse(filesystem['content'])



print_recursively(filesystem)

def print_recursively(items):
    for item in items:
        if isinstance(item, list):
            print_recursively(item)
        else:
            print(item)
