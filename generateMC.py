from sys import argv

import barcode
import requests

import private


def svg(code_list, savepath):
    print('SVG')
    for code in code_list:
        print('generating... ' + savepath + code + '.svg')

        try:
            # generate the svg data of the pattern
            output = barcode.Code39(code, add_checksum=False)
            # save the data as a file
            filename = output.save(savepath + code)
        except:
            print('Error: exception in generating svg')


def emf(code_list, savepath):
    # create svg files to be converted by Cloud Convert REST API
    svg(code_list, savepath)

    # attempt generating emf files
    try:
        print('EMF')
        for code in code_list:
            print('generating...' + savepath + code + '.emf')
            request = requests.post(private.my_api_url,
                                    files={'file': open(savepath + code + '.svg', 'rb')})
            with open(savepath + code + '.emf', 'wb') as fd:
                for chunk in request.iter_content(1024):
                    fd.write(chunk)
    except:
        print('Error: exception in generating emf')


def png(code_list, savepath):
    print('PNG')
    # TODO png support, will require PIL
    pass


def main():
    '''
    Take a list of strings and generate a Code39 barcode in different formats
    :return: none, result is saved as files
    '''
    # list of strings to turn into barcodes
    code_list = []

    if len(argv) == 1:
        # default codes
        code_list = private.default_codes
        svg(code_list, private.savepath)

    elif len(argv) > 1:
        # skip script name and first argument which should be format
        code_list = argv[2:]
        file_format = argv[1]

        # generate vector files according to selected file type
        if file_format == 'svg':
            svg(code_list, private.savepath)
        elif file_format == 'emf':
            emf(code_list, private.savepath)
        elif file_format == 'png':
            png(code_list, private.savepath)


if __name__ == '__main__':
    main()
