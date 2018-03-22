blogs = dict() # blog_name : Blog Object

def menu():
    #Show the user the available blogs
    # Let the user make a choice
    # Do something with the choice
    # Exit from the program
    print_blogs()

def print_blogs():
    for key, blog in blogs.items(): # [(blog_name, Blog), (blog_name, Blog)]
        print('- {}'.format(blog))

