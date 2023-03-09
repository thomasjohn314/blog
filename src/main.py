import web

render = web.template.render('templates/', base='layout')
urls = (
    '/', 'index',
    '/about', 'about',
    '/posts', 'posts',
    '/contact', 'contact'
    )

class index:
    def GET(self):
        return render.index()
    
class about:
    def GET(self):
        return render.about()
    
class posts:
    def GET(self):
        return render.posts()
    
class contact:
    def GET(self):
        return render.contact()

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()