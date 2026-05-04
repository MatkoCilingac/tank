import socket
from web_stranka import web_stranka
from motory import otacanie_hlavy, otacanie_tanku, dopredu_dozadu
from ledky import nastav_jas_led
from zvuk import vystrel

def spusti_server():
    addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)

    print("Web server spustený")

    while True:
        cl = None

        try:
            cl, addr = s.accept()
            request = str(cl.recv(1024))
            print("Požiadavka:", request)

            if "/otacanie_hlavy" in request:
                params = request.split("?")[1].split(" ")[0]
                rychlost = int(params.split("&")[0].split("=")[1])
                smer = params.split("&")[1].split("=")[1]
                otacanie_hlavy(rychlost, smer)

            elif "/otacanie_tanku" in request:
                value = int(request.split("?")[1].split(" ")[0].split("=")[1])
                otacanie_tanku(value)

            elif "/dopredu_dozadu" in request:
                value = int(request.split("?")[1].split(" ")[0].split("=")[1])
                dopredu_dozadu(value)

            elif "/led" in request:
                params = request.split("?")[1].split(" ")[0]
                led = params.split("&")[0].split("=")[1]
                jas = int(params.split("&")[1].split("=")[1])
                nastav_jas_led(led, jas)
            elif "/shoot" in request:
                vystrel()

            cl.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
            cl.send(web_stranka())
            cl.close()

        except Exception as e:
            print("Chyba:", e)

            if cl:
                cl.close()