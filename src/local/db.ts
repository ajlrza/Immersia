import type { generalState, avatarState, avatarPositionState, worldState } from "@/src/src/types/state_types.js"

const dbRequest = indexedDB.open("Database", 1);

let db: any;

dbRequest.onerror = (event) => {
  console.log(event);
  console.error("Error loading database.");
};

dbRequest.onsuccess = (event) => {
  console.log(event);
  console.info("Database initialized.");
  db = (event.target as IDBOpenDBRequest).result;
};

type data_object =
  | { type: "state"; general: generalState }
  | { type: "avatar"; avatar: avatarState }
  | { type: "position"; position: avatarPositionState }
  | { type: "world"; world: worldState };


function processDataWithSwitch(data: data_object) {

    switch (data.type) {
      case "state":
        return data.general;
      case "avatar":
        return data.avatar;
      case "position":
        return data.position;
      case "world":
        return data.world;
    }
}


class DataFactory {
  table: any;
  dbConn: IDBOpenDBRequest;
  db: any;

  readonly pglite_readsql_map = {
    "SELECT": "SELECT"
  };

  constructor(dbConn: IDBOpenDBRequest) {
    this.dbConn = dbConn;
  }

  writeSQL(table?: any, column?: any) {
    let isForTable = false;
    let isForColumn = false;

    const pglite_writesql_map = {

    "CREATE TABLE": "IF NOT EXISTS",

    ...(isForColumn ? { 'ADD COLUMN': (placeholder: string) => "IF NOT EXISTS" } : {}),

    ...(isForTable ? { 'ALTER TABLE': (placeholder: string) => "IF NOT EXISTS" } : {}),

    }

    if (table) {
      isForTable = false;
      isForColumn = true;
    }

    if (column) {
      isForTable = true;
      isForColumn = false;
    }

    if (table && column) {
      return;
    }
  }

  readSQL(table?: any, column?: any) {
    let isForTable = false;
    let isForColumn = false;

    const pglite_writesql_map = {

    "CREATE TABLE": "IF NOT EXISTS",

    ...(isForColumn ? { 'ADD COLUMN': (placeholder: string) => "IF NOT EXISTS" } : {}),

    ...(isForTable ? { 'ALTER TABLE': (placeholder: string) => "IF NOT EXISTS" } : {}),

    }

    if (table) {
      isForTable = false;
      isForColumn = true;
    }

    if (column) {
      isForTable = true;
      isForColumn = false;
    }

    if (table && column) {
      return;
    }
  }
}

const pgTranslate = new PGFactory(dbRequest);
pgTranslate.dbConn = dbRequest;

pgTranslate.dbConn.onupgradeneeded = (event) => {
  pgTranslate.db = (event.target as IDBOpenDBRequest).result;

  for (const [tableName, tableValue] of Object.entries(state_fn_map)) {
    console.log(`Table Name: ${tableName}`);
    console.log(`Table Value:`, tableValue);

    if (!pgTranslate.db.objectStoreNames.contains(tableName)) {
      console.log("Table  already exists.");
      continue;
    } 
    else {
      const tableKey = tableName as TableMapKey;
      const tableTarget = getTableData(tableKey);

      const columns = getTableColumns(tableTarget);
      const columnNames = Object(columns);

      const objectStore = db.createObjectStore(tableName, {
        keyPath: columnNames[0]
      });

      objectStore.createIndex();
      objectStore.createIndex();
      objectStore.createIndex();

    }
  }
};