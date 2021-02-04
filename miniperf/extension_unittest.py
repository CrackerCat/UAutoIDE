from .extension import (
    registered_webview,
    select_app,
    start,
    rpc_get_file_list,
    rpc_gen_cscode,
    rpc_gen_mgrcode,
    rpc_gen_tabfile
)

def main():
    # rpc_get_file_list("I:\I2020_12\TableToolDemo\TableFiles")
    # rpc_gen_cscode("D:\project\TableToolDemo\ConfigTables\Box.xlsx", ".")
    # rpc_gen_mgrcode("D:\project\TableToolDemo\ConfigTables\Box.xlsx", "D:\project\TableToolDemo\Assets\Scripts\TabMgr.cs")
    rpc_gen_tabfile("D:\project\TableToolDemo\ConfigTables\Box.xlsx", "D:\project\TableToolDemo\Assets\StreamingAssets")

if __name__ == "__main__":
    main()

