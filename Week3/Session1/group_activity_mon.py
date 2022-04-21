#Create a Post class with content and the user who posted the content
#Create a User class with name and email and list of posts as attributes
#User should have a method to create a post and add the newest post to the list of posts
#User should have a method to edit the post 
#User should have a method to delete the post
#User should have a method to print all of their posts

class Post:
    def __init__(self, content, user):
        self.content = content
        self.user = user

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.posts = []

    def create_post(self, content):
        # instantiate new post object with method arguments
        new_post = Post(content, self)
        # add newly created post to the list of posts
        self.posts.append(new_post)
        return self

    def delete_post(self, index):
        # check to see if the index is valid for the current list of posts
        # if index is greater than or equal to length of list, then index is out of bounds
        if index < len(self.posts):
            self.posts.pop(index)
        else:
            print("Index is out of bounds")
        return self

    def edit_post(self, content, index):
        if index < len(self.posts):
            post_to_edit = self.posts[index]
            post_to_edit.content = content
        return self

    def print_all_posts(self):
        for post in self.posts:
            print(f"{post.content} POSTED BY {post.user.name}")
        return self

sal = User("Sal", "snast@codingdojo.com")
sal.create_post("Welcome to Python").create_post("Hello World").create_post("I hope you enjoy lecture tonight").print_all_posts().edit_post("Welcome to Coding Dojo", 0).print_all_posts().delete_post(1).print_all_posts()