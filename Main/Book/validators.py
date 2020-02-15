from django.core.exceptions import ValidationError
import datetime
#from Book.models import Book


def page_validator(value):
    if value < 0:
        raise ValidationError(
            (f"Page quantity ({value}) cannot be lower than 0."),
            params={"value": value},
        )


def date_validator(value):    
    for i in value:
        #range of digit positions in unicode is [48:57] "-" in unicode is 45
        if not (58 > ord(i) > 47 or ord(i) == 45):
            raise ValidationError(
            (f"You have placed illegal character in date '{i}'."),
            params={"value": value},
        )
        if len(value) > 10 or len(value) < 4:
            raise ValidationError(
                (f"Too many or too few characters ({value}) pelase check date format."),
                params={"value": value},
        )
        if len(value) == 4 and "-" in  value:
            raise ValidationError(
                (f"You have placed illegal character in date ({value})."),
                params={"value": value},
            )
        if len(value) > 4 and value.count("-") != 2:
            raise ValidationError(
                (f"Please use '-' as a data separator"),
                params={"value": value},
            )
        elif len(value) > 4 and value.count("-") == 2:
            date_elements = value.split("-")
            if len(date_elements[0]) != 4:
                raise ValidationError(
                (f"Please check if year ({date_elements[0]}) were passed correctly."),
                params={"value": value},
                )

            if not (int(date_elements[0]) < (datetime.datetime.now().year + 1) and 0 < int(date_elements[1].replace("0", "")) < 13 and 32 > int(date_elements[2].replace("0", "")) > 0):
                raise ValidationError(
                (f"Please check if number of days or months is not exceeding ther regular number, or if given year is not larger than curreny year."),
                params={"value": value},
                )

    # def book_unique_validator(value):
    #     if Book.objects.filter(ISBN=value):
    #         raise ValidationError(
    #             (f"Book with passed International Standard Book Number ({value}) already exist, please verify number."),
    #             params={"value": value},
    #             )


# def date_validator(value):    
#     for i in value:
#         #range of digit positions in unicode is [48:57] "-" in unicode is 45
#         if not (58 > ord(i) > 47 or ord(i) == 45):
#             raise ValidationError(
#             (f"You have placed illegal character in date '{i}'."),
#             params={"value": value},
#         )
#     if len(value) > 10:
#                 raise ValidationError(
#             (f"Too many characters ({value}) pelase check date format"),
#             params={"value": value},
#         )
#     elif len(value) < 4:
#         raise ValidationError(
#             (f"Not enought characters ({value}) pelase check date format"),
#             params={"value": value},
#         )
    # elif len(value) == 4 and "-" in value:
    #     raise ValidationError(
    #         (f"Please check the date syntax"),
    #         params={"value": value},
    #     )

    # if len(value) > 4 and "-" not in value:
    #     raise ValidationError(
    #         (f"Please use '-' as a data separator"),
    #         params={"value": value},
    #     )
    # elif len(value) > 4 and value.count("-") == 2:
    #     date_elements = value.split("-")  
    #     if len(date_elements[0]) != 4:
    #         raise ValidationError(
    #         (f"Please check if year ({date_elements[0]}) were passed correctly."),
    #         params={"value": value},
    #         )

    #     if not (int(date_elements[0]) < (datetime.datetime.now().year + 1) and 0 < int(date_elements[1].replace("0", "")) < 13 and 32 > int(date_elements[2].replace("0", "")) > 0):
    #         raise ValidationError(
    #         (f"Please check if number of days or months is not exceeding ther regular number, or if given year is not larger than curreny year."),
    #         params={"value": value},
    #         )
    # else:
    #     raise ValidationError(
    #         (f"Please check if full date (including year, month, day) were provided."),
    #         params={"value": value},
    #         )

