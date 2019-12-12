from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):

            if self.path.endswith("/restaurant"):


                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                veggieBurgers = session.query(Restaurant)

                for veggieBurger in veggieBurgers:
                    output = ""
                    output =  veggieBurger.name

                    output += "<html><body>Hello"
                    output += "<html><body>Hello<a href = '/edit'> Edit</a>"

                    output += "</body></html>"

                    newline = "<br>"
                    newline += "<br>"
                    newline += "<br>"
                    self.wfile.write(output)
                    self.wfile.write(newline)


                #print output
                return
            if self.path.endswith("/edit"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hello<a href = '/hello'>back to hello</a>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"

                self.wfile.write(output)
                #print output
            else:
                self.send_error(404, "File not found  %s" % self.path)
    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            print "This is ctype: " + ctype
            print "This is pdict: ", pdict
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                print fields
                messagecontent = fields.get('message')
                print messagecontent
            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output
        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print "Server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "Server shut down..."
        server.socket.close()


if __name__ == '__main__':
    main()
