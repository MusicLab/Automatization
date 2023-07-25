CREATE DATABASE soccrate;


CREATE TABLE clientes (
tid VARCHAR(250) PRIMARY KEY,
nombre_cliente VARCHAR(50) NOT NULL,
region VARCHAR(10) NOT NULL,
token VARCHAR(70) NOT NULL,
aid VARCHAR(70) NOT NULL,
sid VARCHAR(70) NOT NULL,
logo VARCHAR(100) NOT NULL,
periodicidad VARCHAR(10) NOT NULL
licencias bigint NOT NULL,
tipo_producto VARCHAR(50) NOT NULL
);

CREATE TABLE mailsAsociados (
mail VARCHAR(250) NOT NULL,
clientesAsociados TEXT[]

);


CREATE TABLE tokenszoho(
tid VARCHAR(250) PRIMARY KEY,
client_id VARCHAR(250),
refresh_token VARCHAR(250),
sid VARCHAR(250)
)



CREATE TABLE devices (
tid VARCHAR(250),
DeviceName VARCHAR(250),
FOREIGN KEY (tid) REFERENCES clientes(tid),
OperativeSystem VARCHAR(250),
AgentVersion VARCHAR(50) NOT NULL,
Policy VARCHAR(250),
IPs VARCHAR(250),
DateOffline TIMESTAMP,
ZoneName VARCHAR(250),
LastLoggedInUser VARCHAR(250),
Date TIMESTAMP
);


CREATE TABLE threats (
tid VARCHAR(250),
FOREIGN KEY (tid) REFERENCES clientes(tid),	
SHA256 VARCHAR(250),
FileStatus VARCHAR(250) NOT NULL,
DeviceName VARCHAR(250),
FilePath VARCHAR(250),
FileName VARCHAR(250),
Classification VARCHAR(250),
SubClass VARCHAR(250),
FileOwner VARCHAR(250),
DriveType VARCHAR(250),
DateFound TIMESTAMP,
OrigenDeDato VARCHAR(250) NOT NULL
);

CREATE TABLE exploits (
tid VARCHAR(250),
FOREIGN KEY (tid) REFERENCES clientes(tid),
FileName VARCHAR(250),
DeviceName VARCHAR(250),
UserName VARCHAR(250),
ViolationType VARCHAR(250),
Action VARCHAR(250),
FilePath VARCHAR(250),
Created TIMESTAMP,
ProcessID VARCHAR(250)
);



