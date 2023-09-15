import json
import mysql.connector
from fastapi import FastAPI, Request, Response
from sqldata import *
from sqlauth import *


class ProtectiveSecurityData(SqlData):

    def __init__(self):
        super().__init__()

    @staticmethod
    def cast(column, length):
        return " cast(" + column + " as varchar(" + str(length) + ")) as " + column
    @staticmethod
    def psp_section_template_star():
        sql = " id, template_id, section_order, "
        sql += "  cast(section_name as varchar(90)) as section_name, "
        sql += "  cast(video_image as varchar(800)) as video_image, "
        sql += "  cast(title as varchar(200)) as title, "
        sql += "  cast(description_1 as varchar(800)) as description_1, "
        sql += "  cast(description_2 as varchar(800)) as description_2, "
        sql += "  cast(include_photos as varchar(5)) as include_photos, "
        sql += "  cast(include_saa as varchar(5)) as include_saa, "
        sql += "  cast(include_background as varchar(5)) as include_background, "
        sql += "  cast(include_documents as varchar(5)) as include_documents, "
        sql += "  cast(include_comments as varchar(5)) as include_comments "
        return sql

    @staticmethod
    def psp_template_option_star():
        sql = " id, option_id, section_id, parent_id, "
        sql += " cast(option_text as varchar(240)) as option_text, "
        sql += " cast(option_type as varchar(40)) as option_type, "
        sql += " option_order, option_group, "
        sql += " cast(allow_comment as varchar(1)) as allow_comment, "
        sql += " cast(allow_photo as varchar(1)) as allow_photo, "
        sql += " cast(allow_document as varchar(1)) as allow_document "
        return sql

    @staticmethod
    def psp_survey_saa_star():
        sql = " id, survey_id, template_id, option_id, section_id, order_id, user_id, "
        sql += "cast(saa_name as varchar(80)) as saa_name, "
        sql += "cast(saa_type as varchar(80)) as saa_type, "
        sql += "cast(text as varchar(4000)) as text, "
        sql += "cast(system_gen as varchar(1)) as system_gen "
        return sql

    @staticmethod
    def doc_organization_star():
        sql = " id, user_id, "
        sql += ProtectiveSecurityData.cast('org_type',20) + ","
        sql += ProtectiveSecurityData.cast('sub_type',20) + ","
        sql += ProtectiveSecurityData.cast('region_id',20) + ","
        sql += ProtectiveSecurityData.cast('org_name',80) + ","
        sql += ProtectiveSecurityData.cast('contact_name',80) + ","
        sql += ProtectiveSecurityData.cast('mailing_address',80) + ","
        sql += ProtectiveSecurityData.cast('delivery_address',80) + ","
        sql += ProtectiveSecurityData.cast('city',20) + ","
        sql += ProtectiveSecurityData.cast('state',80) + ","
        sql += ProtectiveSecurityData.cast('zip',80) + ","
        sql += ProtectiveSecurityData.cast('telephone',80) + ","
        sql += ProtectiveSecurityData.cast('administrator_name',80) + ","
        sql += ProtectiveSecurityData.cast('internal_code',80) + ","
        sql += ProtectiveSecurityData.cast('internal_org_id',80) + ","
        sql += ProtectiveSecurityData.cast('grades',30) + ","
        sql += ProtectiveSecurityData.cast('state_rep',30) + ","
        sql += ProtectiveSecurityData.cast('state_sen',30) + ","
        sql += ProtectiveSecurityData.cast('fed_cong',30) + ","
        sql += ProtectiveSecurityData.cast('category_id',30) + ","
        sql += ProtectiveSecurityData.cast('nces_id',30) + ","
        sql += ProtectiveSecurityData.cast('website',308) + ","
        sql += ProtectiveSecurityData.cast('county_name',20) + ","
        sql += ProtectiveSecurityData.cast('status',30)
        return sql

    @staticmethod
    def psp_saa_type_star():
        sql = " id, section, ssa_order, "
        sql += ProtectiveSecurityData.cast('options', 80) + ", "
        sql += ProtectiveSecurityData.cast('saa_question', 150) + " "
        return sql


