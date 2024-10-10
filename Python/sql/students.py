from db_context import DBContext

class StudentsDBContext:
    
    def __init__(self,):
        self.db_context = DBContext("students.db")
        self.create_student_db()
        
    
    def create_student_db(self):
        # Erstellt die Datenbank Students
        create_table = """
        CREATE TABLE IF NOT EXISTS Students
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(32) NOT NULL,
            age INTEGER NOT NULL,
            course VARCHAR(32) NOT NULL
        )
        """
        self.db_context.create_database(create_table)
    
    
    # Create
    def add_student(self, name:str, age:int, course:str):
        self.db_context.execute(f"""
                                INSERT INTO Students (name, age, course)
                                values
                                ('{name}',{age},'{course}')
                                """)
    # Read
    def get_student_by_id(self, id:int):
        return self.db_context.execute(f"select * from Students where id = {id}")
    
    def get_all_students(self):
        return self.db_context.execute(f"select * from Students")
    
    # Update
    def update_students(self, id:int, _name:str="", _age:int=0, _course:str=""):
        result = self.get_student_by_id(id)
        
        if len(result) == 0:
            print("Student dont exist")
            return
        
        name = _name
        age = _age
        course = _course
        
        if name == "":
            name = result[0][1]
        
        if age == 0:
            age = result[0][2]
        
        if course == "":
            course = result[0][3]
        
        self.db_context.execute(f"UPDATE Students SET name = '{name}', age = {age}, course = '{course}' where id = {id};")
    
    # Delete
    def delete_student(self, id:int):
        result = self.get_student_by_id(id)
        
        if len(result) == 0:
            print("Student dont exist")
            return
        
        self.db_context.execute(f"DELETE FROM Students where id = {id}")