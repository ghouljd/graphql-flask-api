import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Incident, session

class IncidentType(SQLAlchemyObjectType):
    class Meta:
        model = Incident

class Query(graphene.ObjectType):
    all_incidents = graphene.List(IncidentType)

    def resolve_all_incidents(self, info):
        print("info: ", info.context)
        query = IncidentType.get_query(info)
        return query.all()

class CreateIncident(graphene.Mutation):
    class Arguments:
        description = graphene.String(required=True)
        state = graphene.String(required=True)
        priority = graphene.Int(required=True)
        client = graphene.String(required=True)
        agent = graphene.String(required=True)
        creation_date = graphene.String(required=True)
        update_date = graphene.String(required=True)

    incident = graphene.Field(lambda: IncidentType)

    def mutate(self, info, description,state,priority,client,agent,creation_date,update_date):
        new_incident = Incident(description=description,state=state,priority=priority,client=client,agent=agent,creation_date=creation_date,update_date=update_date)
        session.add(new_incident)
        session.commit()
        return CreateIncident(incident=new_incident)

class Mutation(graphene.ObjectType):
    create_incident = CreateIncident.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
