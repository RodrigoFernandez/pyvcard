import argparse

import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from pyvcard import pyvcard

# https://pyyaml.org/wiki/PyYAMLDocumentation
# https://geekflare.com/es/python-yaml-intro/

# https://docs.python.org/3/library/argparse.html


def crear_qr_qrcode():
    vcard = pyvcard.generar_vcard({'apellido': 'Reiris', 'nombre': 'Gaston', 'prefijo': 'Dr.'}, {'nombre': 'Será Parrilla', 'puesto': 'CEO y Gerente de Baños'},
                                  {'telefono': '4444-5555', 'mail': 'ggreiris@seraparrilla.com.ar', 'site': "https://seraparrilla.netlify.app/"})
    print(vcard)
    pyvcard.generar_qr(vcard, "./qr_ggreiris.png")
    pyvcard.generar_qr(vcard, "./qr_ggreiris_logo.png", "./logo.png")

    pyvcard.generar_qr_svgimage(vcard, "./qr_svgimage.svg")
    pyvcard.generar_qr_svgfragmentImage(vcard, "./qr_svgfragmentImage.svg")
    pyvcard.generar_qr_svgpathimage(vcard, "./qr_svgpathimage.svg")


def crear_qr_segno(datos_vcard):
    vcard = pyvcard.generar_vcard(datos_vcard['titular'],
                                  datos_vcard['empresa'], datos_vcard['contacto'])
    print(vcard)

    for salida in datos_vcard['salidas']:
        pyvcard.generar_vcard_segno(vcard, salida)


def get_argparser():
    parser = argparse.ArgumentParser("Generador qr vcard")
    parser.add_argument("info", help="archivo yaml con la información a procesar")
    return parser


if __name__ == "__main__":
    parser = get_argparser()
    args = parser.parse_args()

    arch_yaml = open(args.info, 'r')
    contenido_yaml = yaml.load(arch_yaml, Loader=Loader)

    crear_qr_segno(contenido_yaml)

# ejemplo de corrida: poetry run python main.py ggreiris.yaml
