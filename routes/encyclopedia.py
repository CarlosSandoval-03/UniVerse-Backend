# Import resources
from controllers.Encyclopedia import (
    Documents,
    AcceptDocument,
    RejectDocument,
    DocumentsByTopic,
)


def add_resources(api):
    api.add_resource(Documents, "/api/community/<int:community_id>/documents")
    api.add_resource(DocumentsByTopic, "/api/topic/<int:topic_id>/documents")
    api.add_resource(RejectDocument, "/api/community/<int:comm_id>/reject_document")
    api.add_resource(AcceptDocument, "/api/community/<int:comm_id>/accept_document")
