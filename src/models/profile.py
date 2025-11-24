from pydantic import BaseModel, EmailStr
from typing import Optional

class PersonalInfo(BaseModel):
    name: str
    email: EmailStr
    phone: str
    location: str
    linkedin: Optional[str] = None

class Language(BaseModel):
    name: str
    level: str

class Skills(BaseModel):
    technical: list[str]
    languages: list[Language]

class Experience(BaseModel):
    company: str
    position: str
    location: str
    start_date: str
    end_date: Optional[str] = None
    description: list[str]

class Education(BaseModel):
    institution: str
    degree: str
    field_of_study: str
    start_date: str
    end_date: Optional[str] = None

class UserProfile(BaseModel):
    personal_info: PersonalInfo
    summary: str
    skills: Skills
    experiences: list[Experience]
    education: list[Education]