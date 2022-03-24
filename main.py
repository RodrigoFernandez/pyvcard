from pyvcard import pyvcard

if __name__ == "__main__":
	#pyvcard.generar_qr("https://seraparrilla.netlify.app/", "./qr_seraparrilla.png")
	vcard = pyvcard.generar_vcard({'apellido': 'Reiris', 'nombre': 'Gaston', 'prefijo': 'Dr.'}, {'nombre': 'Será Parrilla', 'puesto': 'CEO y Gerente de Baños'}, {'telefono': '4444-5555', 'mail': 'ggreiris@seraparrilla.com.ar', 'site': "https://seraparrilla.netlify.app/"})
	print(vcard)
	pyvcard.generar_qr(vcard, "./qr_ggreiris.png")
	
	pyvcard.generar_qr_svgimage(vcard, "./qr_svgimage.svg")
	pyvcard.generar_qr_svgfragmentImage(vcard, "./qr_svgfragmentImage.svg")
	pyvcard.generar_qr_svgpathimage(vcard, "./qr_svgpathimage.svg")
	