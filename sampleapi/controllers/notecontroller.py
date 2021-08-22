from django.core.exceptions import ValidationError
from sampleapi.serializers.notes_serializers import Notes, NotesSerializer

model_fields = ['Title', 'Description', 'Link', 'Image', 'Category']

class NotesController():
    def __init__(self, requests):
        self.info = requests

    def get(self):
        if "_id" in self.info:
            objects = Notes.objects.filter(_id=self.info["_id"])
            if (objects.count() < 1):
                raise ValidationError("No object found with _id as {}".format(self.info["_id"]))
            else:
                note_obj = objects[0]
            return NotesSerializer(note_obj, many=False)
        else:
            page_no = 1
            order_by_created = False
            item_per_page = 10
            if "page" in self.info:
                page_no = self.info["page"]

            if "item_per_page" in self.info:
                item_per_page = self.info["page"]

            if "order_by_created" in self.info:
                order_by_created = True

            start = (page_no - 1) * item_per_page
            end = start + item_per_page

            obj = Notes.objects.all()
            obj_count = obj.count()
            if order_by_created:
                data = obj.order_by("-_created")[start:end]
            else:
                data = obj.order_by("_created")[start:end]

            return {
                "data": NotesSerializer(data, many=True).data,
                "total": obj_count, "order_by": "created"
            }

    def add(self):
        data = {}
        for field in model_fields:
            if field not in self.info:
                raise ValidationError("Missing key '{}'".format(field))
            else:
                data[field] = self.info[field]

        obj = Notes.objects.create(**data)
        return NotesSerializer(obj, many=False).data

    def modify(self):
        if "_id" not in self.info:
            raise ValidationError("Missing Object ID")
        obj = Notes.objects.get(_id=self.info["_id"])
        if obj == None:
            raise ValidationError("Object does not exits check if id is correct")

        for key in model_fields:
            if key in self.info:
                setattr(obj, key, self.info[key])

        obj.save()
        obj = Notes.objects.get(_id=self.info["_id"])
        return NotesSerializer(obj, many=False).data

    def delete(self):
        if "_id" not in self.info:
            raise ValidationError("Missing Object ID")
        Notes.objects.filter(_id=self.info["_id"]).delete()
        return "Object Deleted Successfully"