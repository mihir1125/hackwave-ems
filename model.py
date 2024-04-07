import google.generativeai as genai

genai.configure(api_key='AIzaSyCTyccwplHoEPZQvex6fZAjwPuHmBQGbts')
model = genai.GenerativeModel('gemini-pro')

def get_sql(query):
    prompt = f"""CREATE TABLE employee (
  eid int(11) NOT NULL,
  name varchar(100) NOT NULL,
  date_of_join date NOT NULL,
  mobile_no varchar(20) NOT NULL,
  salary float NOT NULL,
  department varchar(60) NOT NULL,
  designation varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE employee
  ADD PRIMARY KEY (eid);

ALTER TABLE employee
  MODIFY eid int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

CREATE TABLE goals (
  goal_id int(11) NOT NULL,
  goal_description varchar(1024) NOT NULL,
  status tinyint(1) NOT NULL,
  eid int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


ALTER TABLE goals
  ADD PRIMARY KEY (goal_id),
  ADD KEY goals_FK_employee (eid);

ALTER TABLE goals
  MODIFY goal_id int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE goals
  ADD CONSTRAINT goals_FK_employee FOREIGN KEY (eid) REFERENCES employee (eid);
COMMIT;

CREATE TABLE leaves (
  leave_id int(11) NOT NULL,
  leave_type varchar(30) NOT NULL,
  status varchar(30) NOT NULL,
  eid int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

  ADD PRIMARY KEY (leave_id),
  ADD KEY leaves_FK_employee (eid);

ALTER TABLE leaves
  MODIFY leave_id int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE leaves
  ADD CONSTRAINT leaves_FK_employee FOREIGN KEY (eid) REFERENCES employee (eid);
COMMIT;

-- employee.eid can be joined with leaves.eid
-- employee.eid can be joined with goals.eid
--- When searching for string, always use case insensitive like keyword of MySQL

Instruction: Generate SQL query based on these schema
Prompt: {query}

"""
    response = model.generate_content(prompt)
    return "\n".join(response.text.split('\n')[1:-1])