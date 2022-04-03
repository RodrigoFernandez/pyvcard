from pyvcard import pyvcard


def crear_qr_qrcode():
    vcard = pyvcard.generar_vcard({'apellido': 'Reiris', 'nombre': 'Gaston', 'prefijo': 'Dr.'}, {'nombre': 'Será Parrilla', 'puesto': 'CEO y Gerente de Baños'},
                                  {'telefono': '4444-5555', 'mail': 'ggreiris@seraparrilla.com.ar', 'site': "https://seraparrilla.netlify.app/"})
    print(vcard)
    pyvcard.generar_qr(vcard, "./qr_ggreiris.png")
    pyvcard.generar_qr(vcard, "./qr_ggreiris_logo.png", "./logo.png")

    pyvcard.generar_qr_svgimage(vcard, "./qr_svgimage.svg")
    pyvcard.generar_qr_svgfragmentImage(vcard, "./qr_svgfragmentImage.svg")
    pyvcard.generar_qr_svgpathimage(vcard, "./qr_svgpathimage.svg")


def crear_qr_segno():
    vcard = pyvcard.generar_vcard({'apellido': 'Reiris', 'nombre': 'Gaston', 'prefijo': 'Dr.'}, {'nombre': 'Será Parrilla', 'puesto': 'CEO y Gerente de Baños'},
                                  {'telefono': '4444-5555', 'mail': 'ggreiris@seraparrilla.com.ar', 'site': "https://seraparrilla.netlify.app/"})
    print(vcard)
    pyvcard.generar_vcard_segno(vcard, './qr_segno_ggreiris.png')
    pyvcard.generar_vcard_segno(vcard, './qr_segno_ggreiris.svg')


if __name__ == "__main__":
    # crear_qr_qrcode()
    crear_qr_segno()
