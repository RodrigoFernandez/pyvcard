import qrcode
import qrcode.image.svg
import vobject


# https://towardsdatascience.com/generate-qrcode-with-python-in-5-lines-42eda283f325
# https://github.com/lincolnloop/python-qrcode
# https://datatracker.ietf.org/doc/html/rfc6350
# http://eventable.github.io/vobject/


def generar_qr_svg(fuente, destino, factory):
	img = qrcode.make(fuente, image_factory=factory)
	img.save(destino)

def generar_qr_svgimage(fuente, destino):
	generar_qr_svg(fuente, destino, qrcode.image.svg.SvgImage)
	
def generar_qr_svgfragmentImage(fuente, destino):
	generar_qr_svg(fuente, destino, qrcode.image.svg.SvgFragmentImage)
	
def generar_qr_svgpathimage(fuente, destino):
	generar_qr_svg(fuente, destino, qrcode.image.svg.SvgPathImage)

def generar_qr(fuente, destino):
	qr = qrcode.QRCode(version=1, box_size=10, border=5)
	qr.add_data(fuente)
	qr.make(fit=True)
	
	img = qr.make_image(fill='black', back_color='white')
	img.save(destino)

def generar_vcard(titular, empresa, contacto):
	rta = vobject.vCard()
	
	rta.add('n')
	rta.n.value = vobject.vcard.Name(family=titular['apellido'], given=titular['nombre'], prefix=titular['prefijo'])
	
	rta.add('fn')
	rta.fn.value = f"{titular['nombre']} {titular['apellido']}"
	
	rta.add('org')
	rta.org.value = [empresa['nombre']]
	
	rta.add('title')
	rta.title.value = empresa['puesto']
	
	rta.add('tel')
	rta.tel.value = contacto['telefono']
	rta.tel.type_param = 'TRABAJO'
	rta.tel.pref_param = '1'
	
	rta.add('email')
	rta.email.value = contacto['mail']
	rta.email.type_param = 'TRABAJO'
	rta.email.pref_param = '1'
	
	rta.add('url')
	rta.url.value = contacto['site']
	
	return rta.serialize()