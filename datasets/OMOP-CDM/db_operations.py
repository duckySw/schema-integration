from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, TIMESTAMP, ForeignKeyConstraint

# 创建MySQL数据库连接
engine = create_engine('mysql+pymysql://username:password@hostname:port/database_name')

# 创建元数据对象
metadata = MetaData()

# 定义表格
person = Table(
    'person', metadata,
    Column('person_id', Integer, primary_key=True),
    Column('gender_concept_id', Integer, nullable=False),
    Column('race_concept_id', Integer, nullable=False),
    Column('ethnicity_concept_id', Integer, nullable=False),
    Column('location_id', Integer, nullable=True),
    Column('provider_id', Integer, nullable=True),
    Column('care_site_id', Integer, nullable=True),
    # 添加外键约束
    ForeignKeyConstraint(['gender_concept_id'], ['concept.CONCEPT_ID']),
    ForeignKeyConstraint(['race_concept_id'], ['concept.CONCEPT_ID']),
    ForeignKeyConstraint(['ethnicity_concept_id'], ['concept.CONCEPT_ID']),
    ForeignKeyConstraint(['location_id'], ['location.LOCATION_ID']),
    ForeignKeyConstraint(['provider_id'], ['provider.PROVIDER_ID']),
    ForeignKeyConstraint(['care_site_id'], ['care_site.CARE_SITE_ID'])
)

# 创建表格
metadata.create_all(engine)
