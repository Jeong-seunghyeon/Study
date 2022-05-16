select EMPLOYEE_ID as "사번", FIRST_NAME as "이름", JOB_ID as "직위"
from EMPLOYEEs
where JOB_ID='AD_VP' or JOB_ID='FI_ACCOUNT' or JOB_ID='ST_MAN'

select EMPLOYEE_ID as "사번", FIRST_NAME as "이름", JOB_ID as "직위"
from EMPLOYEEs
where JOB_ID in ('AD_VP', 'FI_ACCOUNT', 'ST_MAN') 


select EMPLOYEE_ID as "사번", FIRST_NAME as "이름", JOB_ID as "직위"
from EMPLOYEEs
where JOB_ID not in ('AD_VP', 'FI_ACCOUNT', 'ST_MAN') 

select EMPLOYEE_ID as "사번", FIRST_NAME as "이름", JOB_ID as "직위"
from EMPLOYEEs
where JOB_ID!='AD_VP' or JOB_ID!='FI_ACCOUNT' or JOB_ID!='ST_MAN'
SQL> /

EMPLOYEE_ID FIRST_NAME                               JOB_ID
----------- ---------------------------------------- --------------------
        100 Steven                                   AD_PRES
        103 Alexander                                IT_PROG
        104 Bruce                                    IT_PROG
        105 David                                    IT_PROG
        106 Valli                                    IT_PROG
        107 Diana                                    IT_PROG
        108 Nancy                                    FI_MGR
        114 Den                                      PU_MAN
        115 Alexander                                PU_CLERK
        116 Shelli                                   PU_CLERK
        117 Sigal                                    PU_CLERK

EMPLOYEE_ID FIRST_NAME                               JOB_ID
----------- ---------------------------------------- --------------------
        118 Guy                                      PU_CLERK
        119 Karen                                    PU_CLERK
        125 Julia                                    ST_CLERK
        126 Irene                                    ST_CLERK
        127 James                                    ST_CLERK
        128 Steven                                   ST_CLERK
        129 Laura                                    ST_CLERK
        130 Mozhe                                    ST_CLERK
        131 James                                    ST_CLERK
        132 TJ                                       ST_CLERK
        133 Jason                                    ST_CLERK

EMPLOYEE_ID FIRST_NAME                               JOB_ID
----------- ---------------------------------------- --------------------
        134 Michael                                  ST_CLERK
        135 Ki                                       ST_CLERK
        136 Hazel                                    ST_CLERK
        137 Renske                                   ST_CLERK
        138 Stephen                                  ST_CLERK
        139 John                                     ST_CLERK
        140 Joshua                                   ST_CLERK
        141 Trenna                                   ST_CLERK
        142 Curtis                                   ST_CLERK
        143 Randall                                  ST_CLERK
        144 Peter                                    ST_CLERK

EMPLOYEE_ID FIRST_NAME                               JOB_ID
----------- ---------------------------------------- --------------------
        145 John                                     SA_MAN
        146 Karen                                    SA_MAN
        147 Alberto                                  SA_MAN
        148 Gerald                                   SA_MAN
        149 Eleni                                    SA_MAN
        150 Peter                                    SA_REP
        151 David                                    SA_REP
        152 Peter                                    SA_REP
        153 Christopher                              SA_REP
        154 Nanette                                  SA_REP
        155 Oliver                                   SA_REP

EMPLOYEE_ID FIRST_NAME                               JOB_ID
----------- ---------------------------------------- --------------------
        156 Janette                                  SA_REP
        157 Patrick                                  SA_REP
        158 Allan                                    SA_REP
        159 Lindsey                                  SA_REP
        160 Louise                                   SA_REP
        161 Sarath                                   SA_REP
        162 Clara                                    SA_REP
        163 Danielle                                 SA_REP
        164 Mattea                                   SA_REP
        165 David                                    SA_REP
        166 Sundar                                   SA_REP

EMPLOYEE_ID FIRST_NAME                               JOB_ID
----------- ---------------------------------------- --------------------
        167 Amit                                     SA_REP
        168 Lisa                                     SA_REP
        169 Harrison                                 SA_REP
        170 Tayler                                   SA_REP
        171 William                                  SA_REP
        172 Elizabeth                                SA_REP
        173 Sundita                                  SA_REP
        174 Ellen                                    SA_REP
        175 Alyssa                                   SA_REP
        176 Jonathon                                 SA_REP
        177 Jack                                     SA_REP

EMPLOYEE_ID FIRST_NAME                               JOB_ID
----------- ---------------------------------------- --------------------
        178 Kimberely                                SA_REP
        179 Charles                                  SA_REP
        180 Winston                                  SH_CLERK
        181 Jean                                     SH_CLERK
        182 Martha                                   SH_CLERK
        183 Girard                                   SH_CLERK
        184 Nandita                                  SH_CLERK
        185 Alexis                                   SH_CLERK
        186 Julia                                    SH_CLERK
        187 Anthony                                  SH_CLERK
        188 Kelly                                    SH_CLERK

EMPLOYEE_ID FIRST_NAME                               JOB_ID
----------- ---------------------------------------- --------------------
        189 Jennifer                                 SH_CLERK
        190 Timothy                                  SH_CLERK
        191 Randall                                  SH_CLERK
        192 Sarah                                    SH_CLERK
        193 Britney                                  SH_CLERK
        194 Samuel                                   SH_CLERK
        195 Vance                                    SH_CLERK
        196 Alana                                    SH_CLERK
        197 Kevin                                    SH_CLERK
        198 Donald                                   SH_CLERK
        199 Douglas                                  SH_CLERK

EMPLOYEE_ID FIRST_NAME                               JOB_ID
----------- ---------------------------------------- --------------------
        200 Jennifer                                 AD_ASST
        201 Michael                                  MK_MAN
        202 Pat                                      MK_REP
        203 Susan                                    HR_REP
        204 Hermann                                  PR_REP
        205 Shelley                                  AC_MGR
        206 William                                  AC_ACCOUNT

95 rows selected.