-- 1
SELECT YEAR(billing.charged_datetime) as Year, monthname(billing.charged_datetime) as Month, SUM(billing.amount) as Revenue
FROM billing
WHERE YEAR(billing.charged_datetime) = 2012 AND MONTH(billing.charged_datetime) = 3
GROUP BY MONTH(billing.charged_datetime);

-- 2
SELECT clients.client_id, CONCAT(clients.first_name, " ", clients.last_name) as Client_Name, SUM(billing.amount) as Revenue
FROM clients
LEFT JOIN billing
ON clients.client_id = billing.client_id
WHERE clients.client_id = 2;

-- 3
SELECT clients.client_id, CONCAT(clients.first_name, " ", clients.last_name) as Client_Name, sites.domain_name
FROM clients
LEFT JOIN sites
ON clients.client_id = sites.client_id
WHERE clients.client_id = 10;

-- 4
SELECT clients.client_id, CONCAT(clients.first_name, " ", clients.last_name) as Client_Name, MONTHNAME(sites.created_datetime) as Month, YEAR(sites.created_datetime) as Year, COUNT(sites.domain_name) as Number_of_Websites
FROM clients
LEFT JOIN sites
ON clients.client_id = sites.client_id
WHERE clients.client_id = 1
GROUP BY MONTH(created_datetime), YEAR(created_datetime)
ORDER BY created_datetime;

-- 5
SELECT sites.domain_name, COUNT(leads.first_name), DATE_FORMAT(leads.registered_datetime, "%M %D %Y") 
FROM sites
LEFT JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011/01/01" AND "2011/02/15"
GROUP BY sites.site_id;

-- 6
SELECT CONCAT(clients.first_name, " ", clients.last_name) as Client_Name, COUNT(leads.first_name)
FROM clients
LEFT JOIN sites
ON clients.client_id = sites.client_id
LEFT JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011/01/01" AND "2011/12/31"
GROUP BY clients.client_id;

-- 7
SELECT CONCAT(clients.first_name, " ", clients.last_name) as Client_Name, COUNT(leads.first_name), MONTHNAME(leads.registered_datetime) as Month, YEAR(leads.registered_datetime) as Year
FROM clients
LEFT JOIN sites
ON clients.client_id = sites.client_id
LEFT JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011/01/01" AND "2011/06/30"
GROUP BY leads.leads_id;

-- 8


