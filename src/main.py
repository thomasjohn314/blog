import web
import json
import os

render = web.template.render('templates/', base='layout')
urls = (
    '/', 'index',
    '/home', 'home',
    '/about', 'about',
    '/posts', 'posts',
    '/contact', 'contact'
    )

class index:
    def GET(self):
        raise web.seeother('/home')
    
class home:
    def GET(self):
        return render.home()
    
class about:
    def GET(self):
        return render.about()
    
class posts:
    def GET(self):
        posts = []
        filenames = os.listdir(os.getcwd() + '/posts')
        if len(filenames) == 0:
            return render.error('There are no posts to display.')
        else:
            for filename in filenames:
                f = open('posts/' + filename, 'r')
                posts.append(json.load(f))
                f.close()
            posts = tuple(posts)
            return render.posts(posts)
    
class contact:
    def GET(self):
        return render.contact()

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()