import sys
import grpc
from pydantic import BaseModel, constr, Field, conint, ValidationError, VERSION as PYDANTIC_VERSION, validator
from typing import List
import reporting_pb2
import reporting_pb2_grpc


class Alignment(str):
    Ally = "Ally"
    Enemy = "Enemy"


class Class(str):
    Corvette = "Corvette"
    Frigate = "Frigate"
    Cruiser = "Cruiser"
    Destroyer = "Destroyer"
    Carrier = "Carrier"
    Dreadnought = "Dreadnought"


class Officer(BaseModel):
    first_name: constr(strip_whitespace=True, max_length=100)
    last_name: constr(strip_whitespace=True, max_length=100)
    rank: constr(strip_whitespace=True, max_length=100)


class Spaceship(BaseModel):
    alignment: Alignment
    name: constr(strip_whitespace=True, max_length=100) = Field(
        "Unknown", regex=r"^(?!Enemy$).*$"
    )
    classification: Class
    length: float = Field(..., ge=80.0, le=20000.0)
    crew_size: conint(strict=True, ge=0, le=500)
    armed: bool
    officers: List[Officer]

    @validator("name")
    def validate_name(cls, value, values):
        if values.get("alignment") == "Enemy" and value != "Unknown":
            raise ValueError("Name can only be 'Unknown' for enemy spaceships")
        return value

    @validator("length")
    def validate_length(cls, value):
        if not (80 <= value <= 20000):
            raise ValueError("Invalid spaceship length")
        return value

    @validator("crew_size")
    def validate_crew_size(cls, value):
        if not (0 <= value <= 500):
            raise ValueError("Invalid crew size")
        return value

    class Config:
        extra = "forbid"


def run_client(coordinates):
    channel = grpc.insecure_channel('localhost:50051')
    stub = reporting_pb2_grpc.ReportingStub(channel)
    coordinates_str = ' '.join(coordinates)
    request = reporting_pb2.Coordinates(coordinates=coordinates_str)
    spaceships = stub.GetSpaceships(request)

    for spaceship in spaceships:
        try:
            spaceship_data = {
                "alignment": spaceship.alignment,
                "name": spaceship.name,
                "classification": spaceship.classification,
                "length": spaceship.length,
                "crew_size": spaceship.crew_size,
                "armed": spaceship.armed,
                "officers": [
                    {
                        "first_name": officer.first_name,
                        "last_name": officer.last_name,
                        "rank": officer.rank,
                    }
                    for officer in spaceship.officers
                ],
            }

            try:
                try:
                    version_major = int(PYDANTIC_VERSION.split(".")[0])
                except ValueError:
                    version_major = 0

                if version_major < 2:
                    validated_spaceship = Spaceship(**spaceship_data)
                else:
                    validated_spaceship = Spaceship.validate(**spaceship_data)


                print(validated_spaceship.json(indent=2))

            except ValidationError as e:
                print(f"Invalid spaceship data: {e}")

        except Exception as e:
            print(f"Error processing spaceship: {e}")


if __name__ == '__main__':
    coordinates = sys.argv[1:]
    run_client(coordinates)
