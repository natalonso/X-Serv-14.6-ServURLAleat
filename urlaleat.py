import webapp
import random

class UrlAleat(webapp.webApp): #HEREDAS
    #Heredas una clase, si hay algo más especifico toma lo que le dices aquí, si es igual, usara el proceso de donde lo has heredado.
    def parse(self, request):
        #GET /1/SUMA/2
        recurso=str(request)
        recurso = recurso.split()[1]
        print('RECURSO: ' + recurso)
        if recurso == '/favicon.ico':
            recurso = None

        return recurso

    def process(self, parsedRequest): #recibe peticion paticionada y devuelve una tupla, devuelve una lista, con dos posiciones, codigo y pagina web
    #Process the relevant elements of the request.
    #Returns the HTTP code for the reply, and an HTML page.

        if parsedRequest == "None":
            return ("200 OK", "<html><body><h1>VETE!</h1></body></html>")
        else:
            variable = random.randint(1,1482648)
            return ("200 OK", "<html><body><h1>URL Aleatoria. " + "<a href='http://localhost:1242/" + str(variable) + "'>Dame otra</a>" + "</a></h1></body></html>")

if __name__ == "__main__": #programa principal
    testWebApp = UrlAleat("localhost", 1242)
