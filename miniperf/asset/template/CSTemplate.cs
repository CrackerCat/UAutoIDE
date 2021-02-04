using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Table;
using System.IO;
using System;

namespace Common
{
public partial class Table<TABNAME> : TableFile<TableItem<TABNAME>>
{
    private readonly string TabFilePath = <TABPATH>;

    public bool Init()
    {
        return Load();
    }

    public bool Load()
    {
        // 1st Application.dataPath, 2nd Application.streamingAssetsPath
        var tabFullPath = Application.dataPath + TabFilePath;
        if (!File.Exists(tabFullPath))
        {
            tabFullPath = Application.streamingAssetsPath + TabFilePath;
        }

        return LoadFromFile(tabFullPath, System.Text.Encoding.UTF8);       
    }

    public IEnumerator LoadAsync(string TabConfigPath)
    {
        var handler = GameResources.KResourceManager.LoadAssetAsync<TextAsset>(TabConfigPath + "/" + TabFilePath);

        yield return handler;

        var textAsset = handler.result;
        if (textAsset != null)
        {
            try
            {
                ParseString(textAsset.text);
            }
            catch (Exception e)
            {
                GameDebug.LogError($"【加载配置表失败】 failed to convert Asset type : {TabFilePath} Exception: {e}");
            }

        }
        else
        {
            GameDebug.LogError($"【加载配置表失败】 failed to loadAsset for type : {TabFilePath}");
        }
        yield break;
    }

    public override void HandleLine(TableItem<TABNAME> row)
    {
        //1st_add _dict.Add(row.//MARK_N_PKEY1, row);
        //2nd_add if(!_dict.ContainsKey(row.//MARK_N_PKEY1)) { _dict.Add(row.//MARK_N_PKEY1, new Dictionary<//MARK_T_PKEY2, TableItem<TABNAME>>()); } _dict[row.//MARK_N_PKEY1].Add(row.//MARK_N_PKEY2, row);
    }

    public int Count
    {
        get
        {
            return _dict.Count;
        }
    }
    
    public string keys
    {
        get
        {
            return _dict.Keys.ToString();
        }
    }

    //1st_dec private Dictionary<//MARK_T_PKEY1, TableItem<TABNAME>> _dict = new Dictionary<//MARK_T_PKEY1, TableItem<TABNAME>>();   
    //2nd_dec private Dictionary<//MARK_T_PKEY1, Dictionary<//MARK_T_PKEY2, TableItem<TABNAME>>> _dict = new Dictionary<//MARK_T_PKEY1, Dictionary<//MARK_T_PKEY2, TableItem<TABNAME>>>();
}

public partial class TableItem<TABNAME> : TableFileRow
{
    //public __FILED__ { get; private set; } // __COMMENT__    
//MARK_FILEDS

    internal override void  Parse(string[] cellStrs)
    {          
//MARK_PARSER
    }
}

}//END NameSpace