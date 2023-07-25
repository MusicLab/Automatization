CREATE OR REPLACE FUNCTION exploitsEntreFechas(
	fecha_inicio TIMESTAMP,
	fecha_fin TIMESTAMP,
	tid2 VARCHAR(250)
)
RETURNS SETOF exploits AS $$
BEGIN
  RETURN QUERY
  SELECT *
  FROM exploits
  WHERE Created BETWEEN fecha_inicio AND fecha_fin
  AND tid = tid2;
END;
$$ LANGUAGE plpgsql;



-- -----------------------------------------------------------------


CREATE OR REPLACE FUNCTION threatsEntreFechas(
	fecha_inicio TIMESTAMP,
	fecha_fin TIMESTAMP,
	tid2 VARCHAR(250),
	origendedato2 VARCHAR(250)
)
RETURNS SETOF threats AS $$
BEGIN
  RETURN QUERY
  SELECT *
  FROM threats
  WHERE datefound BETWEEN fecha_inicio AND fecha_fin
  AND tid = tid2
  AND (
    (origendedato2 = 'ClearedEvent' AND (origendedato = 'Cleared' OR origendedato = 'Event'))
    OR
    (origendedato2 = 'ThreatsOnly' AND origendedato = 'Threat')
  );
END;
$$ LANGUAGE plpgsql;

-- -----------------------------------------------

CREATE OR REPLACE FUNCTION devicesEntreFechas(
	fecha_inicio TIMESTAMP,
	fecha_fin TIMESTAMP,
	tid2 VARCHAR(250)
)
RETURNS SETOF devices AS $$
BEGIN
    RETURN QUERY
  SELECT *
  FROM devices
  WHERE date = fecha_fin
  AND tid = tid2;
END;
$$ LANGUAGE plpgsql;




-- -----------------------------------------------------------


CREATE OR REPLACE FUNCTION actualizarCliente(
    cliente_id VARCHAR(70),
    nuevo_nombre VARCHAR(50),
    nueva_region VARCHAR(10),
    nuevo_token VARCHAR(70),
    nuevo_aid VARCHAR(70),
    nuevo_sid VARCHAR(70),
    nuevo_logo VARCHAR(100),
    nueva_periodicidad VARCHAR(10),
    nueva_cant_licencias bigint,
    nuevo_tipo_producto VARCHAR(50)
)
RETURNS VOID AS $$
BEGIN

	IF nuevo_nombre != '' THEN
		UPDATE clientes
		SET nombre_cliente = nuevo_nombre
		WHERE tid = cliente_id;
	END IF;
	
	IF nueva_region != '' THEN
		UPDATE clientes
		SET region = nueva_region
		WHERE tid = cliente_id;
	END IF;
	
	IF nuevo_token != '' THEN
		UPDATE clientes
		SET token = nuevo_token
		WHERE tid = cliente_id;
	END IF;
	
	IF nuevo_aid != '' THEN
		UPDATE clientes
		SET aid = nuevo_aid
		WHERE tid = cliente_id;
	END IF;
	
	IF nuevo_sid != '' THEN
		UPDATE clientes
		SET sid = nuevo_sid
		WHERE tid = cliente_id;
	END IF;
	
	IF nuevo_logo != '' THEN
		UPDATE clientes
		SET logo = nuevo_logo
		WHERE tid = cliente_id;
	END IF;
	
	IF nueva_periodicidad != '' THEN
		UPDATE clientes
		SET periodicidad = nueva_periodicidad
		WHERE tid = cliente_id;
	END IF;

  IF nueva_cant_licencias != '' THEN
		UPDATE clientes
		SET licencias = nueva_cant_licencias
		WHERE tid = cliente_id;
	END IF;

  IF nuevo_tipo_producto != '' THEN
		UPDATE clientes
		SET tipo_producto = nuevo_tipo_producto
		WHERE tid = cliente_id;
	END IF;
	 
END;
$$ LANGUAGE plpgsql;

-- -----------------------------------------------------------------


CREATE OR REPLACE FUNCTION insertar_devices(tid VARCHAR(250), Date TIMESTAMP, data_list JSON[])
RETURNS SETOF devices
LANGUAGE plpgsql
AS $$
DECLARE
  data_item JSON;
  DeviceName VARCHAR(250);
  OperativeSystem VARCHAR(250);
  AgentVersion VARCHAR(250);
  Policy VARCHAR(250);
  IPs VARCHAR(250);
  DateOffline TIMESTAMP;
  ZoneName VARCHAR(250);
  LastLoggedInUser VARCHAR(250);
  
  registro devices%ROWTYPE;
BEGIN
  FOREACH data_item IN ARRAY data_list LOOP
    IF data_item ->> 'DeviceName' IS NULL OR data_item ->> 'DeviceName' = 'None' THEN
      DeviceName := NULL;
    ELSE
      DeviceName := data_item ->> 'DeviceName';
    END IF;
    IF data_item ->> 'OperativeSystem' IS NULL OR data_item ->> 'OperativeSystem' = 'None' THEN
      OperativeSystem := NULL;
    ELSE
      OperativeSystem := data_item ->> 'OperativeSystem';
    END IF;
    AgentVersion := data_item ->> 'AgentVersion';
    Policy := data_item ->> 'Policy';
    IF data_item ->> 'IPs' IS NULL OR data_item ->> 'IPs' = 'None' THEN
      IPs := NULL;
    ELSE
      IPs := data_item ->> 'IPs';
    END IF;
    IF data_item ->> 'DateOffline' IS NULL OR data_item ->> 'DateOffline' = 'None' OR data_item ->> 'DateOffline' = 'Online' THEN
      DateOffline := NULL;
    ELSE
      DateOffline := data_item ->> 'DateOffline';
    END IF;
    ZoneName := data_item ->> 'ZoneName';
    IF data_item ->> 'LastLoggedInUser' IS NULL OR data_item ->> 'LastLoggedInUser' = 'None' THEN
      LastLoggedInUser := NULL;
    ELSE
      LastLoggedInUser := data_item ->> 'LastLoggedInUser';
	END IF;
    INSERT INTO devices (tid, DeviceName, OperativeSystem, AgentVersion, Policy, IPs, DateOffline, ZoneName, LastLoggedInUser, Date)
    VALUES (tid, DeviceName, OperativeSystem, AgentVersion, Policy, IPs, DateOffline, ZoneName, LastLoggedInUser, Date)
    RETURNING * INTO registro;
    RETURN NEXT registro;
  END LOOP;
END;
$$;



-- ------------------------------------exploits



CREATE OR REPLACE FUNCTION insertar_exploits(tid VARCHAR(250), data_list JSON[])
RETURNS SETOF exploits
LANGUAGE plpgsql
AS $$
DECLARE
  data_item JSON;
  DeviceName VARCHAR(250);
  UserName VARCHAR(250);
  ViolationType VARCHAR(250);
  Action VARCHAR(250);
  FilePath VARCHAR(250);
  FileName VARCHAR(250);
  Created TIMESTAMP;
  ProcessID VARCHAR(250);
  
  registro exploits%ROWTYPE;
BEGIN
  FOREACH data_item IN ARRAY data_list LOOP

    IF data_item ->> 'DeviceName' IS NULL OR data_item ->> 'DeviceName' = 'None' THEN
      DeviceName := NULL;
    ELSE
		DeviceName := data_item ->> 'DeviceName';
    END IF;
	
    IF data_item ->> 'UserName' IS NULL OR data_item ->> 'UserName' = 'None' THEN
		UserName := NULL;
    ELSE
      	UserName := data_item ->> 'UserName';
    END IF;
	
    IF data_item ->> 'ViolationType' IS NULL OR data_item ->> 'ViolationType' = 'None' THEN
      ViolationType := NULL;
    ELSE
      ViolationType := data_item ->> 'ViolationType';
    END IF;
	
    IF data_item ->> 'Action' IS NULL OR data_item ->> 'Action' = 'None' THEN
      Action := NULL;
    ELSE
      Action := data_item ->> 'Action';
    END IF;
    
    IF data_item ->> 'FilePath' IS NULL OR data_item ->> 'FilePath' = 'None' THEN
      FilePath := NULL;
    ELSE
      FilePath := data_item ->> 'FilePath';
	END IF;
	
	IF data_item ->> 'FileName' IS NULL OR data_item ->> 'FileName' = 'None' THEN
      FileName := NULL;
    ELSE
      FileName := data_item ->> 'FileName';
	END IF;
	
	IF data_item ->> 'Created' IS NULL OR data_item ->> 'Created' = 'None' THEN
      Created := NULL;
    ELSE
      Created := data_item ->> 'Created';
	END IF;
	
	IF data_item ->> 'ProcessID' IS NULL OR data_item ->> 'ProcessID' = 'None' THEN
      ProcessID := NULL;
    ELSE
      ProcessID := data_item ->> 'ProcessID';
	END IF;
	
    INSERT INTO exploits (tid, DeviceName, UserName, ViolationType, Action, FilePath, FileName, Created, ProcessID)
    VALUES (tid, DeviceName, UserName, ViolationType, Action, FilePath, FileName, Created, ProcessID)
    RETURNING * INTO registro;
    RETURN NEXT registro;
  END LOOP;
END;
$$;


-- ---------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION insertar_threats(tid VARCHAR(250), data_list JSON[])
RETURNS SETOF threats
LANGUAGE plpgsql
AS $$
DECLARE
  data_item JSON;
  SHA256 VARCHAR(250);
  FileStatus VARCHAR(250);
  DeviceName VARCHAR(250);
  FilePath VARCHAR(250);
  FileName VARCHAR(250);
  Classification VARCHAR(250);
  SubClass VARCHAR(250);
  FileOwner VARCHAR(250);
  DriveType VARCHAR(250);
  DateFound TIMESTAMP;
  OrigenDeDato VARCHAR(250);
  registro threats%ROWTYPE;
BEGIN
  FOREACH data_item IN ARRAY data_list LOOP
	
    IF data_item ->> 'SHA256' IS NULL OR data_item ->> 'SHA256' = 'None' THEN
      SHA256 := NULL;
    ELSE
		SHA256 := data_item ->> 'SHA256';
    END IF;
	
	IF data_item ->> 'FileStatus' IS NULL OR data_item ->> 'FileStatus' = 'None' THEN
      FileStatus := NULL;
    ELSE
		FileStatus := data_item ->> 'FileStatus';
    END IF;
	
	IF data_item ->> 'DeviceName' IS NULL OR data_item ->> 'DeviceName' = 'None' THEN
      DeviceName := NULL;
    ELSE
		DeviceName := data_item ->> 'DeviceName';
    END IF;
    
    IF data_item ->> 'FilePath' IS NULL OR data_item ->> 'FilePath' = 'None' THEN
      FilePath := NULL;
    ELSE
      FilePath := data_item ->> 'FilePath';
	END IF;
	
	IF data_item ->> 'FileName' IS NULL OR data_item ->> 'FileName' = 'None' THEN
      FileName := NULL;
    ELSE
      FileName := data_item ->> 'FileName';
	END IF;
	
	IF data_item ->> 'Classification' IS NULL OR data_item ->> 'Classification' = 'None' THEN
      Classification := NULL;
    ELSE
      Classification := data_item ->> 'Classification';
	END IF;
	
	IF data_item ->> 'SubClass' IS NULL OR data_item ->> 'SubClass' = 'None' THEN
      SubClass := NULL;
    ELSE
      SubClass := data_item ->> 'SubClass';
	END IF;
	
	IF data_item ->> 'FileOwner' IS NULL OR data_item ->> 'FileOwner' = 'None' THEN
      FileOwner := NULL;
    ELSE
      FileOwner := data_item ->> 'FileOwner';
	END IF;
	
	IF data_item ->> 'DriveType' IS NULL OR data_item ->> 'DriveType' = 'None' THEN
      DriveType := NULL;
    ELSE
      DriveType := data_item ->> 'DriveType';
	END IF;
	
	IF data_item ->> 'DateFound' IS NULL OR data_item ->> 'DateFound' = 'None' THEN
      DateFound := NULL;
    ELSE
      DateFound := data_item ->> 'DateFound';
	END IF;
	
	IF data_item ->> 'OrigenDeDato' IS NULL OR data_item ->> 'OrigenDeDato' = 'None' THEN
    	OrigenDeDato := NULL;

    ELSE
      OrigenDeDato := data_item ->> 'OrigenDeDato';
	END IF;
	
	
	
    INSERT INTO threats (tid, SHA256, FileStatus, DeviceName, FilePath, FileName, Classification, SubClass, FileOwner, DriveType, DateFound, OrigenDeDato)
    VALUES (tid, SHA256, FileStatus, DeviceName, FilePath, FileName, Classification, SubClass, FileOwner, DriveType, DateFound, OrigenDeDato)
    RETURNING * INTO registro;
    RETURN NEXT registro;
  END LOOP;
END;
$$;


------------------------------------------------------------------------------

CREATE PROCEDURE PUBLIC."insertar_datos_zoho" (
	t_id VARCHAR(250),
	r_token varchar(250),
	s_id varchar(250),
	c_id varchar(250)
)
LANGUAGE plpgsql
as $$
BEGIN
	insert into tokenszoho (tid, refresh_token, sid, cliente_id)
	values (t_id, r_token, s_id, c_id);
END;
$$

------------------------------------------------------------------------------

CREATE PROCEDURE PUBLIC."eliminar_datos" (
  t_id VARCHAR(250)
)
LANGUAGE plpgsql
as $$
BEGIN
    DELETE FROM threats WHERE tid = p_tid;
    DELETE FROM exploits WHERE tid = p_tid;
    DELETE FROM devices WHERE tid = p_tid;
	  DELETE FROM clientes WHERE tid = p_tid;
    -- Agrega más sentencias DELETE si es necesario para más tablas
END;
$$

------------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION get_devices_sin_proteccion (
  fecha TIMESTAMP,
  p_tid VARCHAR(250)
)
RETURNS SETOF devices
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  select * from devices where date = fecha and tid = p_tid
	and (policy ~ 'Fase 1' or policy ~ 'Fase 2' or policy ~ 'Default' or
	(tid = '2473c30c-1c99-429f-9ac3-93d160e37f27' and (policy ~ 'L5' or policy ~ 'L4')));
END;
$$;

------------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION get_devices_sin_zonas (
  fecha TIMESTAMP,
  p_tid VARCHAR(250)
)
RETURNS SETOF devices
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  select * from devices where date = fecha and tid = p_tid and zonename = '["Default"]';
END;
$$;

------------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION get_tokens (
  p_tid VARCHAR(250)
)
RETURNS SETOF devices
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  select * from tokenszoho where tid = p_tid;
END;
$$;

------------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION GetLastLoggedInUsers(
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    device_date TIMESTAMP,
    tid2 VARCHAR(250)
)
RETURNS TABLE(DeviceName VARCHAR, LastLoggedInUser VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT t.DeviceName, d.LastLoggedInUser
    FROM threats t
    LEFT JOIN devices d ON t.DeviceName = d.DeviceName
    WHERE t.DateFound BETWEEN start_date AND end_date
        AND d.Date = device_date
        AND t.tid = tid2
        AND (t.origendedato = 'Cleared' OR t.origendedato = 'Event');
END;
$$ LANGUAGE plpgsql;


---------------------------------------------------------------------------

CREATE FUNCTION getExploitCount(
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    tidEspecifico VARCHAR DEFAULT NULL
)
RETURNS TABLE (fecha DATE, tid VARCHAR(250), cantidad BIGINT)
AS
$$
BEGIN
    IF tidEspecifico IS NULL THEN
        RETURN QUERY
        SELECT DATE(created) AS fecha,
               NULL::VARCHAR(250) AS tid,
               COUNT(*) AS cantidad
        FROM exploits
        WHERE created BETWEEN start_date AND end_date
        GROUP BY DATE(created);
    ELSE
        RETURN QUERY
        SELECT DATE(created) AS fecha,
               exploits.tid AS tid,
               COUNT(*) AS cantidad
        FROM exploits
        WHERE created BETWEEN start_date AND end_date
            AND exploits.tid = tidEspecifico
        GROUP BY DATE(created), exploits.tid;
    END IF;
END;
$$
LANGUAGE plpgsql;

-----------------------------------------------------------------



CREATE FUNCTION getDeviceCount(
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    tidEspecifico VARCHAR DEFAULT NULL
)
RETURNS TABLE (fecha DATE, tid VARCHAR(250), cantidad BIGINT)
AS
$$
BEGIN
    IF tidEspecifico IS NULL THEN
        RETURN QUERY
        SELECT DATE(date) AS fecha,
               NULL::VARCHAR(250) AS tid,
               COUNT(*) AS cantidad
        FROM devices
        WHERE date BETWEEN start_date AND end_date
        GROUP BY DATE(date);
    ELSE
        RETURN QUERY
        SELECT DATE(date) AS fecha,
               devices.tid AS tid,
               COUNT(*) AS cantidad
        FROM devices
        WHERE date BETWEEN start_date AND end_date
            AND devices.tid = tidEspecifico
        GROUP BY DATE(date), devices.tid;
    END IF;
END;
$$
LANGUAGE plpgsql;
   
------------------------------------------------------------------

CREATE FUNCTION getThreatOnlyCount(
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    tidEspecifico VARCHAR DEFAULT NULL
)
RETURNS TABLE (fecha DATE, tid VARCHAR(250), cantidad BIGINT)
AS
$$
BEGIN
    IF tidEspecifico IS NULL THEN
        RETURN QUERY
        SELECT DATE(datefound) AS fecha,
               NULL::VARCHAR(250) AS tid,
               COUNT(*) AS cantidad
        FROM threats
        WHERE datefound BETWEEN start_date AND end_date
            AND origendedato = 'Threat'
        GROUP BY DATE(datefound);
    ELSE
        RETURN QUERY
        SELECT DATE(datefound) AS fecha,
               threats.tid AS tid,
               COUNT(*) AS cantidad
        FROM threats
        WHERE datefound BETWEEN start_date AND end_date
            AND origendedato = 'Threat'
            AND threats.tid = tidEspecifico
        GROUP BY DATE(datefound), threats.tid;
    END IF;
END;
$$
LANGUAGE plpgsql;

---------------------------------------------------------------------------

CREATE FUNCTION getClearedEventCount(
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    tidEspecifico VARCHAR DEFAULT NULL
)
RETURNS TABLE (fecha DATE, tid VARCHAR(250), cantidad BIGINT)
AS
$$
BEGIN
    IF tidEspecifico IS NULL THEN
        RETURN QUERY
        SELECT DATE(datefound) AS fecha,
               NULL::VARCHAR(250) AS tid,
               COUNT(*) AS cantidad
        FROM threats
        WHERE datefound BETWEEN start_date AND end_date
            AND (origendedato = 'Cleared' OR origendedato = 'Event')
        GROUP BY DATE(datefound);
    ELSE
        RETURN QUERY
        SELECT DATE(datefound) AS fecha,
               threats.tid AS tid,
               COUNT(*) AS cantidad
        FROM threats
        WHERE datefound BETWEEN start_date AND end_date
            AND (origendedato = 'Cleared' OR origendedato = 'Event')
            AND threats.tid = tidEspecifico
        GROUP BY DATE(datefound), threats.tid;
    END IF;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION contar_threats_devicename(
  tid_param VARCHAR(250), 
  start_date_param DATE, 
  end_date_param DATE,
  filestatus_param VARCHAR(250)
)
RETURNS TABLE (FileName VARCHAR(250), FilePath VARCHAR(250), DeviceName VARCHAR(250), Count BIGINT)
AS $$
BEGIN
    RETURN QUERY
    SELECT threats.FileName, threats.FilePath, threats.DeviceName, COUNT(*) AS Count
    FROM threats
    WHERE tid = tid_param 
      AND DateFound BETWEEN start_date_param AND end_date_param
      AND (origendedato = 'Cleared' OR origendedato = 'Event')
      AND filestatus = filestatus_param
    GROUP BY threats.FileName, threats.FilePath, threats.DeviceName;
END;
$$
LANGUAGE plpgsql;


----------------------------------------------------------------------------------




						


