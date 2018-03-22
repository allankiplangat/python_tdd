MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to crate a post, or "q" to quit: '
blogs = dict() # blog_name : Blog Object

def menu():
    #Show the user the available blogs
    # Let the user make a choice
    # Do something with the choice
    # Exit from the program
    print_blogs()
    selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items(): # [(blog_name, Blog), (blog_name, Blog)]
        print('- {}'.format(blog))

