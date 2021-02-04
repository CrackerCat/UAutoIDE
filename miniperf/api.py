import glob
import subprocess
import webview
import os
from miniperf import extension

class Api:
    def pywebviewready(self):
        print('pywebviewready')
    
    def on_HomeClick(self):
        print('on_HomeClick')
        
    def fullscreen(self):
        webview.windows[0].toggle_fullscreen()

    def save_content(self, content):
        filename = webview.windows[0].create_file_dialog(webview.SAVE_DIALOG)
        print(filename)
        if not filename:
            return

        with open(filename, 'w') as f:
            f.write(content)

    def ls(self):
        print('ls')
        return os.listdir('.')


    def get_file_list(xlsxpath):
        file_list = []
        try:
            files_status = extension.get_svn_status(xlsxpath)
            print(files_status)

            files = glob.glob(xlsxpath + '/**/*.xls*', recursive=True)
            for f in files:
                if not os.path.basename(f).startswith('~'):
                    status = files_status.get(f, 'o')
                    file_list.append({'name': os.path.basename(f), 'path': f, 'status': status})

            
            # list = output.replace(' ', '')
            # list = list[2:]
            # list = list.split(r'\n')        
            # for f in list:
            #     name = f[1:-2].split(r'\\')[-1]
            #     if 'xls' in name and not name.startswith('~'):
            #         file_list.append({'name': name, 'path': f[1:-2].replace('\\\\','\\'), 'status':f[0]})
        except Exception as e:
            print(e)
            files = glob.glob(xlsxpath + '/**/*.xls*', recursive=True)
            for f in files:
                if not os.path.basename(f).startswith('~'):
                    file_list.append({'name': os.path.basename(f), 'path': f, 'status':'o'})
        # print(xlsxpath)
        # files = glob.glob(xlsxpath + '/**/*.xls*', recursive=True)
        # for f in files:
        #     if not os.path.basename(f).startswith('~'):
        #             file_list.append({'name': os.path.basename(f), 'path': f})
        print(file_list)
        return file_list