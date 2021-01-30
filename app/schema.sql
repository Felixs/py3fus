DROP TABLE IF EXISTS urls;
DROP TABLE IF EXISTS hits;

CREATE TABLE "urls" (
	"id"	INTEGER NOT NULL,
	"short"	TEXT NOT NULL UNIQUE,
	"long"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

INSERT INTO "main"."urls" ("id", "short", "long") VALUES ('1', 'about', 'https://github.com/Felixs/py3fus');

CREATE TABLE "hits" (
	"id"	INTEGER NOT NULL UNIQUE,
	"hits"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("id") REFERENCES "urls"("id")
);

INSERT INTO "main"."hits" ("id", "hits") VALUES ('1', '0');

