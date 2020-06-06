from flask_restful import Resource, reqparse
from db import query

class Emp(Resource):
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('empno', type=int, required=True, help='Cannot be blank')
        data= parser.parse_args()
        try:
            return query(f"""Select * from testapi.emp where empno={data["empno"]}""")
        except:
            return {"message": "There was an error connecting to emp table"}, 500

    def post(self):
        parser= reqparse.RequestParser()
        parser.add_argument('empno', type=int, required=True, help="empno Cannot be blank")
        parser.add_argument('ename', type=str, required=True, help="empname Cannot be blank")
        parser.add_argument('job', type=str, required=True, help="job Cannot be blank")
        parser.add_argument('mgr', type=int, required=True, help=" mgr Cannot be blank")
        parser.add_argument('hiredate', type=str, required=True, help="hiredate Cannot be blank")
        parser.add_argument('sal', type=str, required=True, help="sal Cannot be blank")
        parser.add_argument('comm', type=str)
        parser.add_argument('deptno', type=int, required=True, help="deptno Cannot be blank")
        parser.add_argument('pass', type=str, required=True, help="pass Cannot be blank")
        data=parser.parse_args()
        try:
            x=query(f"""select * from testapi.emp where empno={data['empno']}""", return_json=False)
            if len(x)>0:
                return {"message": "An emp with that name already exists"}, 400
        except:
            return {message:"There was an error"}, 500
        if data['comm']!=None:
            try:
                query(f"""insert into testapi.emp values({data['empno']},
                '{data['ename']}','{data['job']}', {data['mgr']}, '{data['hiredate']}',
                '{data['sal']}', '{data['comm']}',{data['deptno']},'{data['pass']}'
                )""")
            except:
                return {"message": "There was an error inserting into emp table"}, 500
            return {"message": "Success"}, 201
        else:
            try:
                query(f"""insert into testapi.emp (empno, ename, job, mgr, hiredate, sal, deptno, pass)
            values({data['empno']},
            '{data['ename']}','{data['job']}', {data['mgr']}, '{data['hiredate']}',
            '{data['sal']}',{data['deptno']},'{data['pass']}'
            )""")
            except:
                return {"message": "There was an error inserting into emp table"}, 500
            return {"message": "Success"}, 201


        try:
            query(f"""insert into testapi.emp values({data['empno']},
            '{data['ename']}','{data['job']}', {data['mgr']}, '{data['hiredate']}',
            '{data['sal']}', '{data['comm']}',{data['deptno']},'{data['pass']}'
            )""")
        except:
            return {"message": "There was an error inserting into emp table"}, 500
        return {"message": "Success"}, 201