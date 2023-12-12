DROP DATABASE IF EXISTS PersonList5X;
CREATE DATABASE IF NOT EXISTS PersonList5X
	CHARACTER SET utf8;
USE PersonList5X;

-- segno zodiacale
DROP TABLE IF EXISTS Zodiac;
CREATE TABLE IF NOT EXISTS Zodiac (
	id	INT	PRIMARY KEY	AUTO_INCREMENT,
	name	VARCHAR(12)	NOT NULL,
	kind	ENUM('fire', 'earth', 'air', 'water')	NOT NULL,
	fromDate	DATE	NOT NULL	DEFAULT CURRENT_DATE,
	toDate	DATE	NOT NULL	DEFAULT CURRENT_DATE,
	UNIQUE(name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO Zodiac(fromDate, toDate, name, kind) VALUES
	(CONCAT(YEAR(NOW()), '-03-21'),	CONCAT(YEAR(NOW()), '-04-19'),	'Aries',	'fire'),
	(CONCAT(YEAR(NOW()), '-04-20'),	CONCAT(YEAR(NOW()), '-05-20'),	'Taurus',	'earth'),
	(CONCAT(YEAR(NOW()), '-05-21'),	CONCAT(YEAR(NOW()), '-06-22'),	'Gemini',	'air'),
	(CONCAT(YEAR(NOW()), '-06-21'),	CONCAT(YEAR(NOW()), '-07-22'),	'Cancer',	'water'),
	(CONCAT(YEAR(NOW()), '-07-23'),	CONCAT(YEAR(NOW()), '-08-23'),	'Leo',	'fire'),
	(CONCAT(YEAR(NOW()), '-08-24'),	CONCAT(YEAR(NOW()), '-09-22'),	'Virgo',	'earth'),
	(CONCAT(YEAR(NOW()), '-09-23'),	CONCAT(YEAR(NOW()), '-10-22'),	'Libra',	'air'),
	(CONCAT(YEAR(NOW()), '-10-23'),	CONCAT(YEAR(NOW()), '-11-21'),	'Scorpio',	'water'),
	(CONCAT(YEAR(NOW()), '-11-22'),	CONCAT(YEAR(NOW()), '-12-21'),	'Sagittarius',	'fire'),
	(CONCAT(YEAR(NOW()), '-12-22'),	CONCAT(YEAR(NOW()), '-01-19'),	'Capricorn',	'earth'),
	(CONCAT(YEAR(NOW()), '-01-20'),	CONCAT(YEAR(NOW()), '-02-19'),	'Aquarius',	'air'),
	(CONCAT(YEAR(NOW()), '-02-20'),	CONCAT(YEAR(NOW()), '-03-20'),	'Pisces',	'water');

-- Gruppo sanguineo
DROP TABLE IF EXISTS Blood;
CREATE TABLE IF NOT EXISTS Blood (
	id	INT	PRIMARY KEY	AUTO_INCREMENT,
	-- gruppo sanquineo
	kind	ENUM('A', 'B', 'O', 'AB')	NOT NULL	DEFAULT 'O',
	-- fattore Rh
	rh	ENUM('-', '+')	NOT NULL	DEFAULT '-',
	-- chiave candidata
	UNIQUE(kind, rh)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO Blood(kind, rh) VALUES
	('A',	'-'),
	('A',	'+'),
	('B',	'-'),
	('B',	'+'),
	('O',	'-'),
	('O',	'+'),
	('AB',	'-'),
	('AB',	'+');

-- Città in elenco
DROP TABLE IF EXISTS Cities;
CREATE TABLE IF NOT EXISTS Cities (
	id	INT	PRIMARY KEY	AUTO_INCREMENT,
	name	VARCHAR(30) NOT NULL,
	-- provincia
	country	CHAR(2)	NOT NULL	DEFAULT 'NA',
	-- CAP
	zipcode	INT(5)	NOT NULL,
	-- Codice catastale
	code	CHAR(4)	NOT NULL,

	CHECK(zipcode BETWEEN 10000 AND 99999),

	UNIQUE(name, country),
	UNIQUE(zipcode, code),
	UNIQUE(code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO Cities(zipcode, code, name, country) VALUES
	(80053,	'C129',	'Castellammare di Stabia',	'NA'),
	(80030,	'C188',	'Castello di Cisterna',	'NA'),
	(80028,	'E224',	'Grumo Nevano',	'NA'),
	(84018,	'I483',	'Scafati',	'SA'),
	(80056,	'H243',	'Ercolano',	'NA'),
	(80069,	'L485',	'Vico Equense',	'NA'),
	(80040,	'I978',	'Striano',	'NA'),
	(80040,	'M115',	'Volla',	'NA'),
	(80010,	'H114',	'Quarto',	'NA'),
	(81031,	'A512',	'Aversa',	'CE'),
	(80013,	'B905',	'Casalnuovo di Napoli',	'NA'),
	(80055,	'G902',	'Portici',	'NA'),
	(80035,	'F924',	'Nola',	'NA'),
	(80021,	'A064',	'Afragola',	'NA'),
	(80051,	'A068',	'Agerola',	'NA'),
	(80041,	'B076',	'Boscoreale',	'NA'),
	(80040,	'M280',	'Trecase',	'NA'),
	(80047,	'H860',	'San Giuseppe Vesuviano',	'NA'),
	(80010,	'G309',	'Villaricca',	'NA'),
	(80045,	'G813',	'Pompei',	'NA'),
	(80040,	'I151',	'San Sebastiano al Vesuvio',	'NA'),
	(80023,	'B371',	'Caivano',	'NA'),
	(80039,	'I469',	'Saviano',	'NA'),
	(80042,	'B077',	'Boscotrecase',	'NA'),
	(84100,	'H703',	'Salerno',	'SA'),
	(80030,	'B565',	'Camposano',	'NA'),
	(84059,	'B476',	'Camerota',	'SA'),
	(80059,	'L259',	'Torre del Greco',	'NA'),
	(80030,	'I540',	'Scisciano',	'NA'),
	(80077,	'E329',	'Ischia',	'NA'),
	(80063,	'G568',	'Piano di Sorrento',	'NA'),
	(80058,	'L245',	'Torre Annunziata',	'NA'),
	(84011,	'A251',	'Amalfi',	'SA'),
	(84012,	'A294',	'Angri',	'SA'),
	(81043,	'B715',	'Capua',	'CE'),
	(80031,	'B227',	'Brusciano',	'NA'),
	(80033,	'C675',	'Cicciano',	'NA'),
	(80024,	'B759',	'Cardito',	'NA'),
	(80012,	'B452',	'Calvizzano',	'NA'),
	(80036,	'G283',	'Palma Campania',	'NA'),
	(80018,	'F799',	'Mugnano di Napoli',	'NA'),
	(80026,	'B990',	'Casoria',	'NA'),
	(80020,	'D170',	'Crispano',	'NA'),
	(84091,	'A717',	'Battipaglia',	'SA'),
	(80070,	'A535',	'Bacoli',	'NA'),
	(81022,	'B860',	'Casagiove',	'CE'),
	(80040,	'C495',	'Cercola',	'NA'),
	(84010,	'C984',	'Corbara',	'SA'),
	(80050,	'B980',	'Casola di Napoli',	'NA'),
	(80025,	'B925',	'Casandrino',	'NA'),
	(80030,	'L460',	'Tufino',	'NA'),
	(80065,	'I208',	"Sant'Agnello",	'NA'),
	(80030,	'E954',	'Mariglianella',	'NA'),
	(80074,	'B924',	'Casamicciola Terme',	'NA'),
	(80027,	'D789',	'Frattamaggiore',	'NA'),
	(80020,	'D790',	'Frattaminore',	'NA'),
	(80038,	'G795',	"Pomigliano d'Arco",	'NA'),
	(80030,	'I391',	'San Vitaliano',	'NA'),
	(81024,	'E791',	'Maddaloni',	'CE'),
	(80079,	'H072',	'Procida',	'NA'),
	(80020,	'B946',	'Casavatore',	'NA'),
	(80040,	'G765',	'Pollena Trocchia',	'NA'),
	(80040,	'L142',	'Terzigno',	'NA'),
	(80061,	'F030',	'Massa Lubrense',	'NA'),
	(80034,	'E955',	'Marigliano',	'NA'),
	(80029,	'I293',	"Sant'Antimo",	'NA'),
	(80100,	'F839',	'Napoli',	'NA'),
	(84013,	'C361',	'Cava dei Tirreni',	'SA'),
	(80050,	'E557',	'Lettere',	'NA'),
	(80040,	'G762',	'Poggiomarino',	'NA'),
	(84014,	'F912',	'Nocera Inferiore',	'SA'),
	(80057,	'I300',	"Sant'Antonio Abate",	'NA'),
	(80078,	'G964',	'Pozzuoli',	'NA'),
	(80049,	'I820',	'Somma Vesuviana',	'NA'),
	(80017,	'F111',	'Melito di Napoli',	'NA'),
	(80016,	'E906',	'Marano di Napoli',	'NA'),
	(80050,	'G670',	'Pimonte',	'NA'),
	(80062,	'F162',	'Meta',	'NA'),
	(80044,	'G190',	'Ottaviano',	'NA'),
	(80030,	'C697',	'Cimitile',	'NA'),
	(80022,	'A455',	'Arzano',	'NA'),
	(80048,	'I262',	"Sant'Anastasia",	'NA'),
	(80046,	'H892',	'San Giorgio a Cremano',	'NA'),
	(80050,	'M273',	'Santa Maria la Carità',	'NA'),
	(80011,	'A024',	'Acerra',	'NA'),
	(80014,	'E054',	'Giugliano in Campania',	'NA'),
	(80054,	'E131',	'Gragnano',	'NA'),
	(80071,	'A268',	'Anacapri',	'NA'),
	(80067,	'I862',	'Sorrento',	'NA'),
	(80070,	'F488',	'Monte di Procida',	'NA');

-- Sesso: forse codificheremo anche persone di sesso non binario
DROP TABLE IF EXISTS Gender;
CREATE TABLE IF NOT EXISTS Gender (
	id	INT	PRIMARY KEY	AUTO_INCREMENT,
	kind	CHAR(1)	NOT NULL	DEFAULT 'm',

	UNIQUE(kind)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO Gender(kind) VALUES
	('m'),
	('f');

-- Persone
DROP TABLE IF EXISTS People;
CREATE TABLE IF NOT EXISTS People (
	id	INT	PRIMARY KEY	AUTO_INCREMENT,
	lastname	VARCHAR(18)	NOT NULL,
	firstname	VARCHAR(18)	NOT NULL,
	-- codice fiscale
	code CHAR(16)	NOT NULL,
	-- sesso
	gender	INT	NOT NULL	DEFAULT 1,
	-- data di nascita
	birthday	DATE	NOT NULL	DEFAULT CURRENT_DATE,
	-- altezza (cm)
	height	INT(3)	NOT NULL	DEFAULT 170,
	-- peso	(kg)
	weight	FLOAT(4,1)	NOT NULL	DEFAULT 70.5,
	-- gruppo sanquineo
	fk_blood	INT	NOT NULL	DEFAULT	5,
	-- numero di cellulare
	mobile	CHAR(13),
	-- paese di nascita
	bornplace	INT	NOT NULL,

	UNIQUE(code),
	UNIQUE(firstname, lastname, gender, birthday),

	-- non posso nascere nel futuro!!!
	CHECK (birthday <= CURRENT_DATE),
	CHECK (height >= 110),
	CHECK (weight >= 30.5),

	FOREIGN KEY (gender) REFERENCES Gender(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	FOREIGN KEY (fk_blood) REFERENCES Blood(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	FOREIGN KEY (bornplace) REFERENCES Cities(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO People(lastname, firstname, code, gender, birthday, height, weight, fk_blood, mobile, bornplace) VALUES
	('Sorrentino',	'Virginia',	'SRRVGN06T46I862I',	2,	'2006-12-06',	168,	57.9,	8,	'+393379992794',	89),
	('Gargiulo',	'Bianca',	'GRGBNC94L44G283I',	2,	'1994-07-04',	170,	57.9,	2,	'+393387131627',	40),
	('De Luca',	'Alberto',	'DLCLRT06R29M273A',	1,	'2006-10-29',	179,	71.7,	4,	'+393422815128',	84),
	('Cozzolino',	'Giuseppina',	'CZZGPP93R56E954M',	2,	'1993-10-16',	165,	82.1,	2,	'+393301943843',	53),
	('Napolitano',	'Gennaro',	'NPLGNR97P17F912H',	1,	'1997-09-17',	190,	72.9,	6,	'+393380715314',	71),
	('Scognamiglio',	'Barbara',	'SCGBBR04A52G902R',	2,	'2004-01-12',	175,	57.3,	6,	'+393174182840',	12),
	('Capasso',	'Giovanna',	'CPSGNN07H41L460X',	2,	'2007-06-01',	156,	78.0,	6,	'+393435428975',	51),
	('Giordano',	'Ciro',	'GRDCRI96S13A294X',	1,	'1996-11-13',	182,	105.7,	2,	'+393575768327',	34),
	('Cirillo',	'Simona',	'CRLSMN01R61C129M',	2,	'2001-10-21',	169,	85.8,	6,	'+393610816540',	1),
	('De Simone',	'Leonardo',	'DSMLRD06M01I483S',	1,	'2006-08-01',	169,	66.2,	4,	'+393102294261',	4),
	('Vitiello',	'Ilaria',	'VTLLRI99P67L259C',	2,	'1999-09-27',	172,	78.5,	2,	'+393824049583',	28),
	('Ferrara',	'Achille',	'FRRCLL05B19C675Q',	1,	'2005-02-19',	164,	82.0,	5,	'+393495794219',	37),
	('Palumbo',	'Agata',	'PLMGTA95M45E557W',	2,	'1995-08-05',	160,	95.2,	6,	'+393599692821',	69),
	('Di Stefano',	'Daniela',	'DSTDNL02C67A268E',	2,	'2002-03-27',	162,	64.6,	4,	'+393483191206',	88),
	('De Lucia',	'Antonio',	'DLCNTN94C21C984F',	1,	'1994-03-21',	175,	78.4,	4,	'+393371314667',	48),
	('Izzo',	'Gloria',	'ZZIGLR95A63E791I',	2,	'1995-01-23',	161,	96.1,	4,	'+393855411219',	59),
	('Merola',	'Maria',	'MRLMRA05M70G309V',	2,	'2005-08-30',	161,	67.1,	6,	'+393582090624',	19),
	('Piscitelli',	'Anna',	'PSCNNA05D62B227E',	2,	'2005-04-22',	169,	66.1,	2,	'+393258217783',	36),
	('Marino',	'Giuseppe',	'MRNGPP01C03I540P',	1,	'2001-03-03',	182,	105.9,	5,	'+393390477140',	29),
	('De Rosa',	'Lucia',	'DRSLCU95A58A064J',	2,	'1995-01-18',	154,	48.0,	6,	'+393978347426',	14),
	("D'Angelo",	'Giorgia',	'DNGGRG97L62L245B',	2,	'1997-07-22',	164,	75.5,	1,	'+393155791288',	32),
	('Romagnoli',	'Carmela',	'RMGCML03A02H243V',	1,	'2003-01-02',	186,	75.9,	6,	'+393699276592',	5),
	('Piccirillo',	'Renata',	'PCCRNT99C61B925O',	2,	'1999-03-21',	175,	49.3,	2,	'+393746798425',	50),
	('Esposito',	'Viola',	'SPSVLI00R44G670T',	2,	'2000-10-04',	154,	90.7,	2,	'+393614129408',	77),
	('Russo',	'Celeste',	'RSSCST95H59M280K',	2,	'1995-06-19',	175,	58.0,	6,	'+393799098255',	17),
	('Coppola',	'Umberto',	'CPPMRT07L01A251G',	1,	'2007-07-01',	157,	80.3,	2,	'+393948783348',	33),
	('Barbato',	'Donatella',	'BRBDTL99C48H892N',	2,	'1999-03-08',	165,	93.0,	5,	'+393564305064',	83),
	('Iodice',	'Cristina',	'DCICST95H69I300R',	2,	'1995-06-29',	170,	88.9,	2,	'+393210728224',	72),
	('Papa',	'Laura',	'PPALRA07T42B452L',	2,	'2007-12-02',	173,	78.0,	4,	'+393528432473',	39),
	('Palmieri',	'Luana',	'PLMLNU98T68E224P',	2,	'1998-12-28',	171,	98.5,	4,	'+393379417633',	3),
	('Pagano',	'Tiziano',	'PGNTZN02D13B924F',	1,	'2002-04-13',	186,	57.7,	8,	'+393604652675',	54),
	('Senatore',	'Francesco',	'SNTFNC05B23I978G',	1,	'2005-02-23',	188,	89.3,	6,	'+393595498380',	7),
	('Ruggiero',	'Aurora',	'RGGRRA94E64B476F',	2,	'1994-05-24',	169,	52.8,	6,	'+393419481700',	27),
	('Landi',	'Clemente',	'LNDCMN00R19B076I',	1,	'2000-10-19',	178,	60.5,	4,	'+393137556571',	16),
	('Apicella',	'Gerardo',	'PCLGRD06M14B990P',	1,	'2006-08-14',	171,	68.8,	6,	'+393259817360',	42),
	('De Martino',	'Roberto',	'DMRRRT06S13E329C',	1,	'2006-11-13',	159,	72.3,	2,	'+393620588179',	30),
	('Sarnelli',	'Angelo',	'SRNNGL96E03E906P',	1,	'1996-05-03',	171,	61.7,	6,	'+393746333151',	76),
	('Vitale',	'Alessandro',	'VTLLSN01D02G190V',	1,	'2001-04-02',	174,	64.3,	6,	'+393952327791',	79),
	('Grimaldi',	'Francesca',	'GRMFNC03B47H860F',	2,	'2003-02-07',	165,	79.0,	6,	'+393665738704',	46),
	('Lamberti',	'Gianna',	'LMBGNN06S56G762Y',	2,	'2006-11-16',	172,	42.4,	6,	'+393899705820',	70),
	('Amato',	'Alessia',	'MTALSS99P42D170C',	2,	'1999-09-02',	164,	62.5,	4,	'+393926120333',	43),
	('Calabrese',	'Arcangelo',	'CLBRNG96S22B077B',	1,	'1996-11-22',	187,	104.7,	2,	'+393781322749',	24),
	('Veropalumbo',	'Tamara',	'VRPTMR95A53I469L',	2,	'1995-01-13',	175,	99.2,	6,	'+393599634374',	23),
	('Buonocore',	'Amelia',	'BNCMLA99H41I208N',	2,	'1999-06-01',	165,	98.2,	6,	'+393282326679',	52),
	('Cavaliere',	'Anastasia',	'CVLNTS94M52I262W',	2,	'1994-08-12',	154,	75.4,	8,	'+393381544023',	82),
	('Conte',	'Simone',	'CNTSMN06P18F799H',	1,	'2006-09-18',	179,	63.6,	6,	'+393113704039',	41),
	('Vollono',	'Paolo',	'VLLPLA06T57F111P',	2,	'2006-12-17',	174,	81.6,	1,	'+393986982884',	75),
	('Romano',	'Isabella',	'RMNSLL03B54H114E',	2,	'2003-02-14',	175,	80.7,	6,	'+393888942882',	9),
	('Donnarumma',	'Mauro',	'DNNMRA08C21B905H',	1,	'2008-03-21',	177,	75.9,	6,	'+393347208672',	11),
	('Aprea',	'Valeria',	'PRAVLR94C51B371J',	2,	'1994-03-11',	163,	76.7,	6,	'+393785354450',	22),
	('Martinelli',	'Catello',	'MRTCLL98B24A512V',	1,	'1998-02-24',	184,	60.9,	6,	'+393562239570',	10),
	('Malafronte',	'Raffaele',	'MLFRFL94A29G812H',	1,	'1994-01-29',	187,	61.8,	1,	'+393449633609',	57),
	('Cannavacciuolo',	'Aldo',	'CNNLDA05P12F924E',	1,	'2005-09-12',	184,	88.8,	6,	'+393596069046',	13),
	('Carbone',	'Alessio',	'CRBLSS98E02F162S',	1,	'1998-05-02',	180,	73.6,	2,	'+393395072407',	78),
	('Cannavale',	'Spartaco',	'CNNSRT97P18L845Z',	1,	'1997-09-18',	177,	96.5,	4,	'+393928223992',	6),
	('Scarpato',	'Priscilla',	'SCRPSC97M46G795F',	2,	'1997-08-06',	169,	84.3,	4,	'+393220990019',	62),
	('Savarese',	'Giacomo',	'SVRGCM08B20A068Y',	1,	'2008-02-20',	161,	56.5,	2,	'+393788019497',	15),
	('Alfano',	'Dalila',	'LFNDLL99C62A024B',	2,	'1999-03-22',	155,	65.2,	6,	'+393287088004',	85),
	('Vanacore',	'Dario',	'VNCDRA98H16F488M',	1,	'1998-06-16',	183,	74.8,	6,	'+393621509287',	90),
	('Manzo',	'Carolina',	'MNZCLN02E65B565H',	2,	'2002-05-25',	151,	72.3,	8,	'+393308716093',	26),
	('Di Maio',	'Marco',	'DMIMRC97H09L142Q',	1,	'1997-06-09',	177,	63.6,	6,	'+393193875991',	63),
	('Visciano',	'Luigina',	'VSCLGN04H53H931H',	2,	'2004-06-13',	162,	79.2,	2,	'+393695039306',	18),
	('Nappo',	'Moira',	'NPPMRO99B43A535M',	2,	'1999-02-03',	165,	62.1,	8,	'+393944482364',	45),
	('Caputo',	'Immacolata',	'CPTMCL08R41H703K',	2,	'2008-10-01',	161,	36.9,	2,	'+393818559938',	25),
	('Amitrano',	'Emanuela',	'MTRMNL96S62E054B',	2,	'1996-11-22',	175,	71.4,	6,	'+393339814264',	86),
	('Santarpia',	'Donata',	'SNTDNT96B61G964A',	2,	'1996-02-21',	163,	98.7,	2,	'+393692011513',	73),
	('Arpino',	'Veronica',	'RPNVNC07P64I293L',	2,	'2007-09-24',	161,	46.0,	2,	'+393593361864',	66),
	('Langella',	'Rosaria',	'LNGRSR04T53A717O',	2,	'2004-12-13',	165,	61.7,	4,	'+393159420043',	44),
	('Sabatino',	'Vincenzo',	'SBTVCN00H03D790R',	1,	'2000-06-03',	184,	95.4,	6,	'+393251844391',	56),
	('Maresca',	'Andrea',	'MRSNDR98R16M115H',	1,	'1998-10-16',	184,	83.1,	4,	'+393615902809',	8),
	('Amendola',	'Carlo',	'MNDCRL95P28C188I',	1,	'1995-09-28',	174,	79.7,	5,	'+393688640030',	2),
	('Scazzillo',	'Egidio',	'SCZGDE94A27B759N',	1,	'1994-01-27',	175,	60.5,	4,	'+393197550255',	38),
	('Di Nocera',	'Laura',	'DNCLRA05A54B946C',	2,	'2005-01-14',	159,	63.5,	2,	'+393956822331',	61),
	('Cioffi',	'Renato',	'CFFRNT98M10H072S',	1,	'1998-08-10',	181,	85.5,	8,	'+393420211685',	60),
	('Imparato',	'Domenico',	'MPRDNC02P04C495K',	1,	'2002-09-04',	178,	85.9,	6,	'+393559561739',	47),
	('Cascone',	'Terenzio',	'CSCTNZ02B16I820L',	1,	'2002-02-16',	171,	94.3,	6,	'+393756135625',	74),
	('De Gregorio',	'Ornella',	'DGRRLL98M43I151U',	2,	'1998-08-03',	173,	62.5,	4,	'+393247659324',	21),
	('Sicignano',	'Rita',	'SCGRTI05P63E955D',	2,	'2005-09-23',	170,	73.3,	2,	'+393410370129',	65),
	('Finamore',	'Franco',	'FNMFNC04P02I391E',	1,	'2004-09-02',	182,	79.3,	4,	'+393384582265',	58),
	('Cuomo',	'Massimiliano',	'CMUMSM04C23F839G',	1,	'2004-03-23',	189,	58.1,	6,	'+393965515508',	67),
	('Del Gaudio',	'Rachele',	'DLGRHL07H59B980E',	2,	'2007-06-19',	155,	60.6,	4,	'+393641182394',	49),
	('Somma',	'Giancarlo',	'SMMGCR97B16C697B',	1,	'1997-02-16',	168,	84.2,	2,	'+393677011386',	80),
	('Vicedomini',	'Susanna',	'VCDSNN97H64G568S',	2,	'1997-06-24',	163,	79.0,	4,	'+393610160717',	31),
	('Criscuolo',	'Giuliana',	'CRSGLN05A62D789U',	2,	'2005-01-22',	168,	54.6,	6,	'+393555166058',	55),
	('Farnese',	'Claudio',	'FRNCLD02E27G813T',	1,	'2002-05-27',	168,	91.9,	3,	'+393931657158',	20),
	('Zurolo',	'Cesare',	'ZRLCSR08A01F030R',	1,	'2008-01-01',	157,	66.6,	1,	'+393494878648',	64),
	('Tufano',	'Marilena',	'TFNMLN03R70B715Q',	2,	'2003-10-30',	171,	76.8,	4,	'+393669508107',	35),
	('Apuzzo',	'Michela',	'PZZMHL01B47E131R',	2,	'2001-02-07',	175,	49.1,	2,	'+393401485441',	87),
	('Pappalardo',	'Stella',	'PPPSLL08B44A455Z',	2,	'2008-02-04',	149,	37.5,	2,	'+393515703442',	81),
	('Schettino',	'Paola',	'SCHPLA99M58C361H',	2,	'1999-08-18',	172,	64.7,	4,	'+393356197966',	68);

-- Residenza e cambio residenza
DROP TABLE IF EXISTS Place2Live;
CREATE TABLE IF NOT EXISTS Place2Live (
	id	INT	PRIMARY KEY	AUTO_INCREMENT,
	-- chiave esterna alla specifica persona
	people	INT	NOT NULL,
	-- posto in cui vive
	place	INT	NOT NULL,
	-- data in cui la persona si è trasferita
	dt	DATE	NOT NULL	DEFAULT CURRENT_DATE,

	-- non posso trasferirmi in una nuova casa in una data futura
	CHECK (dt <= CURRENT_DATE),

	-- non posso vivere contemporaneamente in due posti differenti
	UNIQUE(people, place, dt),
	FOREIGN KEY (people) REFERENCES People(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	FOREIGN KEY (place) REFERENCES Cities(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO Place2Live(people, place, dt) VALUES
	(1,	90,	'2022-02-02'),
	(2,	39,	'2018-03-01'),
	(3,	85,	'2022-01-30'),
	(4,	51,	'2020-05-13'),
	(5,	70,	'2022-03-13'),
	(6,	11,	'2020-05-02'),
	(7,	51,	'2007-06-01'),
	(8,	34,	'1996-11-13'),
	(9,	1,	'2001-10-21'),
	(10,	4,	'2006-08-01'),
	(11,	28,	'1999-09-27'),
	(12,	36,	'2021-10-04'),
	(13,	67,	'2017-06-13'),
	(14,	89,	'2019-09-21'),
	(15,	46,	'2011-03-03'),
	(16,	57,	'2014-04-11'),
	(17,	19,	'2005-08-30'),
	(18,	35,	'2022-04-05'),
	(19,	31,	'2020-08-08'),
	(20,	13,	'2018-09-12'),
	(21,	34,	'2015-05-05'),
	(22,	1,	'2021-12-30'),
	(23,	49,	'2021-05-25'),
	(24,	75,	'2018-04-02'),
	(25,	17,	'1995-06-19'),
	(26,	33,	'2007-07-01'),
	(27,	84,	'2022-01-11'),
	(28,	71,	'2011-07-14'),
	(29,	39,	'2007-12-02'),
	(30,	20,	'2017-09-21'),
	(31,	54,	'2002-04-13'),
	(32,	6,	'2021-03-26'),
	(33,	26,	'2010-06-27'),
	(34,	15,	'2021-09-23'),
	(35,	41,	'2022-07-24'),
	(36,	30,	'2006-11-13'),
	(37,	75,	'2018-05-04'),
	(38,	79,	'2001-04-02'),
	(39,	46,	'2003-02-07'),
	(40,	68,	'2022-05-16'),
	(41,	45,	'2016-05-29'),
	(42,	23,	'2018-01-27'),
	(43,	21,	'2019-05-27'),
	(44,	54,	'2017-04-21'),
	(45,	80,	'2020-02-06'),
	(46,	39,	'2022-10-06'),
	(47,	73,	'2022-09-24'),
	(48,	8,	'2022-02-04'),
	(49,	13,	'2021-12-28'),
	(50,	22,	'1994-03-11'),
	(51,	9,	'2017-02-06'),
	(52,	58,	'2013-05-10'),
	(53,	14,	'2021-10-13'),
	(54,	78,	'1998-05-02'),
	(55,	8,	'2016-11-21'),
	(56,	61,	'2016-06-21'),
	(57,	14,	'2022-09-28'),
	(58,	85,	'1999-03-22'),
	(59,	88,	'2015-06-29'),
	(60,	26,	'2002-05-25'),
	(61,	64,	'2017-10-07'),
	(62,	17,	'2022-03-11'),
	(63,	44,	'2017-11-18'),
	(64,	24,	'2022-07-09'),
	(65,	85,	'2022-08-06'),
	(66,	72,	'2019-01-21'),
	(67,	68,	'2017-05-02'),
	(68,	46,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(69,	55,	'2022-02-26'),
	(70,	7,	'2018-02-09'),
	(71,	1,	'2019-01-08'),
	(72,	36,	'2021-12-18'),
	(73,	61,	'2005-01-14'),
	(74,	62,	'2022-09-27'),
	(75,	47,	'2002-09-04'),
	(76,	75,	'2021-04-14'),
	(77,	21,	'1998-08-03'),
	(78,	66,	CURRENT_DATE - INTERVAL FLOOR(3*RAND()) MONTH),
	(79,	60,	CURRENT_DATE - INTERVAL FLOOR(6*RAND()) MONTH),
	(80,	67,	'2004-03-23'),
	(81,	48,	CURRENT_DATE - INTERVAL FLOOR(6*RAND()) MONTH),
	(82,	78,	'2017-03-19'),
	(83,	32,	'2017-09-20'),
	(84,	54,	'2021-10-02'),
	(85,	4,	'2022-06-21'),
	(86,	64,	'2008-01-01'),
	(87,	34,	'2022-09-01'),
	(88,	1,	'2022-08-20'),
	(89,	83,	'2022-09-12'),
	(90,	67,	'2018-01-01');

-- Luoghi in cui si lavora o in cui si ha lavorato
DROP TABLE IF EXISTS Place2Job;
CREATE TABLE IF NOT EXISTS Place2Job (
	id	INT	PRIMARY KEY	AUTO_INCREMENT,
	-- chiave esterna alla specifica persona
	people	INT	NOT NULL,
	-- posto in cui lavora (se null è inoccupato)
	place	INT,
	-- data in cui la persona ha iniziato il lavoro
	dt	DATE	NOT NULL	DEFAULT CURRENT_DATE,

	CHECK (dt <= CURRENT_DATE),

	FOREIGN KEY (people) REFERENCES People(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	FOREIGN KEY (place) REFERENCES Cities(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO Place2Job(people, place, dt) VALUES
	(1,	90,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(2,	39,	'2012-05-20'),
	(3,	86,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(4,	53,	'2022-02-20'),
	(5,	71,	'2015-10-21'),
	(6,	11,	'2022-07-31'),
	(7,	53,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(8,	33,	'2015-07-12'),
	(9,	1,	'2022-02-21'),
	(10,	4,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(11,	28,	'2019-03-16'),
	(12,	36,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(13,	68,	'2016-09-11'),
	(14,	90,	'2021-03-10'),
	(15,	48,	'2016-06-27'),
	(16,	59,	'2013-01-04'),
	(17,	19,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(18,	35,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(19,	31,	'2022-07-12'),
	(20,	15,	'2017-03-29'),
	(21,	32,	'2022-05-09'),
	(23,	49,	'2020-12-17'),
	(24,	75,	'2019-07-12'),
	(25,	16,	'2017-08-10'),
	(26,	34,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(27,	84,	'2017-02-03'),
	(28,	71,	'2020-03-14'),
	(29,	39,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(30,	4,	'2018-04-03'),
	(31,	54,	'2021-08-03'),
	(33,	28,	'2015-03-12'),
	(34,	16,	'2019-01-15'),
	(35,	40,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(36,	29,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(37,	75,	'2021-08-27'),
	(38,	79,	'2021-05-29'),
	(39,	46,	'2022-01-18'),
	(40,	68,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(41,	45,	'2020-01-11'),
	(42,	23,	'2019-08-21'),
	(43,	21,	'2020-03-17'),
	(44,	53,	'2021-01-31'),
	(45,	80,	'2017-11-04'),
	(46,	1,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(47,	73,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(48,	9,	'2021-07-16'),
	(50,	23,	'2019-01-05'),
	(51,	10,	'2020-04-06'),
	(52,	59,	'2015-10-20'),
	(53,	15,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(54,	78,	'2017-10-31'),
	(55,	7,	'2015-07-07'),
	(56,	61,	'2021-09-05'),
	(58,	84,	'2021-08-06'),
	(59,	90,	'2021-05-01'),
	(60,	24,	'2020-05-04'),
	(61,	62,	'2017-03-21'),
	(62,	19,	'2022-08-20'),
	(63,	46,	'2022-05-17'),
	(65,	87,	'2017-06-10'),
	(66,	72,	'2022-08-21'),
	(68,	45,	'2022-09-20'),
	(69,	55,	'2020-06-09'),
	(70,	7,	'2021-08-10'),
	(71,	3,	'2019-10-22'),
	(72,	38,	'2013-04-09'),
	(73,	60,	CURRENT_DATE - INTERVAL FLOOR(21*RAND()) DAY),
	(74,	61,	'2017-11-27'),
	(75,	46,	'2022-02-06'),
	(77,	21,	'2022-01-08'),
	(79,	59,	'2022-08-13'),
	(80,	68,	'2022-09-16'),
	(82,	79,	'2019-10-14'),
	(85,	4,	'2020-09-02'),
	(87,	36,	'2022-05-07'),
	(88,	1,	'2022-01-09');