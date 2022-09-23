from .definitions import Media
import strawberry
from typing import List
from strawberry.types import Info
from strawberry.file_uploads import Upload
from .resolvers import upload_media
@strawberry.input
class MediaInput:
    files: List[Upload]
    ref: str
    refId: str
    field: str

@strawberry.input
class FolderInput:
    files: List[Upload]
    ref: str
    refId: str
    field: str
    

@strawberry.type
class MediaMutation:
   
    
    @strawberry.mutation
    async def read_file(self, file: Upload) -> str:
        return await file.read()

    @strawberry.mutation
    async def read_files(self, media: FolderInput, info: Info) -> Media:
        request = info.context["request"]
        print("Files:", media)
        contents = []
      
        media = upload_media(media, headers=request.headers)
        return Media.from_instance(media)
        
    
 
   

