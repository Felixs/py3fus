
CREATE TABLE IF NOT EXISTS "urls" (
	"short"	TEXT NOT NULL UNIQUE,
	"long"	TEXT NOT NULL,
	"hits"	INTEGER NOT NULL DEFAULT 0,
	"valid_until"	INTEGER NOT NULL DEFAULT 0,
	"active"	INTEGER NOT NULL DEFAULT 1,
	PRIMARY KEY("short")
);

INSERT INTO "main"."urls" ("short", "long") VALUES ('about', 'https://github.com/Felixs/py3fus');


