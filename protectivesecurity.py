import json
import mysql.connector
from fastapi import FastAPI, Request, Response
from sqldata import *
from sqlauth import *
from protectivesecurity_data import *


class ProtectiveSecurity(SqlData):

    def __init__(self):
        super().__init__()

    @staticmethod
    def show_tables():
        return SqlData.sql("select * from nua_user")

    @staticmethod
    def get_survey_asset_section(post_data):

        asset_id = post_data['data']['asset_id']

        sql = "select org_id from nua_user where id = " + str(post_data['uid'])
        rs = SqlData.sql0(sql)
        org_id = rs['org_id']

        sql = "select * from doc_organization where id = " + str(org_id)
        o = SqlData.sql0(sql)

        sql = "select " + ProtectiveSecurityData.psp_survey_saa_star() + " from "
        sql += "psp_survey_saa where id = " + str(asset_id)
        asset = SqlData.sql0(sql)
        saa_type = asset['saa_type']

        sql = "select * from psp_saa_type where id = " + saa_type
        saatype = SqlData.sql0(sql)

        i = post_data['data']['section_id']

        sql = "select id, template_id, section_order, "
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
        sql += "  from psp_template_section where id = " + str(i)

        sql = "select id, template_id, section_order, "
        sql += "  section_name, "
        sql += "  cast(video_image as varchar(800)) as video_image, "
        sql += "  cast(title as varchar(200)) as title, "
        sql += "  description_1, "
        sql += "  cast(description_2 as varchar(800)) as description_2, "
        sql += "  cast(include_photos as varchar(5)) as include_photos, "
        sql += "  cast(include_saa as varchar(5)) as include_saa, "
        sql += "  cast(include_background as varchar(5)) as include_background, "
        sql += "  cast(include_documents as varchar(5)) as include_documents, "
        sql += "  cast(include_comments as varchar(5)) as include_comments "
        sql += "  from psp_template_section where id = " + str(i)

        section = SqlData.sql0(sql)


        sql = "SELECT id, option_id, section_id, parent_id, "
        sql += " cast(option_text as varchar(240)) as option_text, cast(option_type as varchar(40)), "
        sql += " option_order, option_group FROM psp_template_option WHERE "
        sql += " section_id = " + str(i) + " AND parent_id = 0 AND "
        sql += " asset_id = " + str(saa_type) + " ORDER BY option_order"
        return { "sql": sql}
        # sections = {}

        questions = SqlData.sql(sql)

        output = {"org": o, "section": section, "questions": questions, "asset": asset}
        output['saa_type'] = saatype
        output['saa_type_name'] = saa_type
        return output

    @staticmethod
    def get_survey_section(post_data):

        sql = "select org_id from nua_user where id = " + str(post_data['uid'])
        rs = SqlData.sql0(sql)
        org_id = rs['org_id']

        sql = "select * from doc_organization where id = " + str(org_id)
        o = SqlData.sql0(sql)

        i = post_data['data']['section_id']

        sql = "select id, template_id, section_order, "
        sql += "  section_name, "
        sql += "  cast(video_image as varchar(800)) as video_image, "
        sql += "  title, "
        sql += "  cast(description_1 as varchar(800)) as description_1, "
        sql += "  cast(description_2 as varchar(800)) as description_2, "
        sql += "  cast(include_photos as varchar(5)) as include_photos, "
        sql += "  cast(include_saa as varchar(5)) as include_saa, "
        sql += "  cast(include_background as varchar(5)) as include_background, "
        sql += "  cast(include_documents as varchar(5)) as include_documents, "
        sql += "  cast(include_comments as varchar(5)) as include_comments "
        sql += "  from psp_template_section where id = " + str(i)
        sections = SqlData.sql(sql)

        sql = "SELECT id, option_id, section_id, parent_id, "
        sql += " cast(option_text as varchar(240)) as option_text, cast(option_type as varchar(40)), "
        sql += " option_order, option_group FROM psp_template_option WHERE "
        sql += "section_id = " + str(i) + " AND parent_id = 0 AND asset_id = 0 ORDER BY option_order"

        # sections = {}

        questions = SqlData.sql(sql)

        sql = "select id, survey_id, template_id, option_id, section_id, order_id, user_id, "
        sql += "cast(saa_name as varchar(80)) as saa_name, "
        sql += "cast(text as varchar(4000)) as text, "
        sql += "cast(system_gen as varchar(1)) as system_gen "
        sql += "from psp_survey_saa where section_id = " + str(i)
        sql += " and survey_id = " + str(org_id)
        sql += " order by saa_type"
        saa = SqlData.sql(sql)

        output = {"org": o, "sections": sections, "questions": questions, "saa": saa}
        return output

    @staticmethod
    def get_survey_home(post_data):
        user = SqlAuth.get_user(post_data)
        sql = "select id, template_id, section_order, "
        sql += "  cast(section_name as varchar(90)) as section_name, "
        sql += "  cast(video_image as varchar(800)) as video_image, "
        sql += "  cast(title as varchar(200)) as title, "
        sql += "  cast(description_1 as varchar(800)) as description_1, "
        sql += "  cast(description_2 as varchar(800)) as description_2, "
        sql += "  cast(include_photos as varchar(5)) as include_photos, "
        sql += "  cast(include_saa as varchar(5)) as include_saa, "
        sql += "  cast(include_background as varchar(5)) as include_background, "
        sql += "  cast(include_documents as varchar(5)) as include_documents, "
        sql += "  cast(include_comments as varchar(5)) as include_comments from "
        sql += "  psp_template_section order by section_order"
        rs = SqlData.sql(sql)

        if 'id2' not in post_data:
            post_data['data'] = {"section_id": "10"}
            post_data['section_id'] = post_data['id2']
        else:
            post_data['data'] = {"section_id": post_data['id2']}
            post_data['section_id'] = post_data['id2']

        if 'section_id' not in post_data['data']:
            post_data['data']['section_id']="10"

        output = ProtectiveSecurity.get_survey_section(post_data)
        output['section_id'] = post_data['data']['section_id']
        output['section_list'] = rs
        output['user'] = user
        output['current_section'] = ProtectiveSecurity.get_survey_section(post_data)
        return output

    @staticmethod
    def get_survey_main_menu(post_data):
        sql = "select id, cast(section_name as VARCHAR(90)) as section_name, 'N' as active, '' as badge "
        sql += " from psp_template_section where template_id = 0 order by section_order"
        rs = SqlData.sql(sql)
        output = {"list": rs}
        return output

    @staticmethod
    def get_stakeholder_info(post_data):
        output = {}
        rs = SqlData.sql("select * from psp_stakeholder where id = " + post_data['data']['stakeholder_id'])
        if len(rs) > 0:
            form_data = {}
            output['formData'] = form_data
        else:
            output['formData'] = {}
            output['facilities'] = {}
        return output

    @staticmethod
    def get_survey_section_background(data):

        sql = "select * from nua_user where id = " + str(data['uid'])
        r = SqlData.sql0(sql)

        org_id = r['org_id']

        sql = "select " + ProtectiveSecurityData.doc_organization_star() + " from "
        sql += "doc_organization where id = " + str(org_id)

        org = SqlData.sql0(sql)

        output = {"org": org }

        section_id = data['data']['section_id']
        sql = "SELECT " + ProtectiveSecurityData.psp_saa_type_star() + " FROM psp_saa_type "
        sql += " WHERE section = " + str(section_id)
        sql += " order by options"
        rs = SqlData.sql(sql)

        output['saa_types'] = rs

        sql = "SELECT * FROM psp_survey_participant WHERE survey_id = " + str(org_id)
        rs = SqlData.sql(sql)
        output['participants'] = rs

        saa_form_data = {"section_id": section_id, "survey_id": org_id }

        sql = "SELECT id, saa_question FROM psp_saa_type WHERE section = " + str(section_id)
        sql += " and saa_question <> '' order by ssa_order"
        rs = SqlData.sql(sql)

        for record in rs:
            sql = "SELECT " + ProtectiveSecurityData.psp_survey_saa_star() + " from psp_survey_saa "
            sql += " where survey_id = " + str(org_id) + " and saa_type = " + str(record['id'])
            r = SqlData.sql0(sql)
            if r is None:
                saa_form_data['p' + str(record['id'])] = "Y"
            else:
                saa_form_data['p' + str(record['id'])] = ""


        output['saaFormData'] = saa_form_data
        output['saa_options'] = rs

        sql = "SELECT * FROM psp_photo_type WHERE section = " + str(section_id)
        sql += " order by options"
        rs = SqlData.sql(sql)
        output['photo_types'] = rs

        sql = "SELECT * FROM psp_document_type WHERE section = " + str(section_id)
        sql += " order by options"
        rs = SqlData.sql(sql)
        output['document_types'] = rs

        sql = "SELECT * FROM psp_survey_photo WHERE survey_id = " + str(org_id)
        sql += " and section_id = " + str(section_id)
        rs = SqlData.sql(sql)

        photos = []
        for record in rs:
            if record['photo_type'] == '':
                record['photo_type'] = '0'
            sql = "select full_name from nua_user where id = " + str(record['user_id'])
            m = SqlData.sql0(sql)
            if m is None:
                record['user_name'] = 'Not found'
            else:
                record['user_name'] = m['full_name']

            sql = "select options from psp_photo_type where id = " + str(record['photo_type'])
            m = SqlData.sql0(sql)
            if m is None:
                record['type_name'] = ''
            else:
                record['type_name'] = m['options']

            photos.append(record)

        output['photos'] = photos

        sql = "SELECT * FROM psp_survey_document WHERE survey_id = " + str(org_id)
        sql += " and section_id = " + str(section_id)

        rs = SqlData.sql(sql)

        photos = []

        for record in rs:
            sql = "select options from psp_document_type where id = " + str(record['document_type'])
            s = SqlData.sql0(sql)
            if s is None:
                record['type_name'] = ""
            else:
                record['type_name'] = s['options']

            sql = "SELECT * FROM nua_user WHERE id = " + str(record['user_id'])
            s = SqlData.sql0(sql)
            if s is None:
                record['full_name'] = "Not Found"
            else:
                record['full_name'] = s['full_name']

            photos.append(record)

        output['documents'] = photos

        # rs = SqlData.sql(sql)

        sql = "SELECT * FROM psp_survey_comment WHERE option_id = 0 and asset_id = 0 and survey_id = " + str(org_id)
        sql += " and section_id = " + str(section_id)
        rs = SqlData.sql(sql)
        photos = []

        for record in rs:
            sql = "SELECT * FROM nua_user WHERE id = " + str(record['user_id'])
            s = SqlData.sql0(sql)
            if s is None:
                record['full_name'] = "Not Found"
            else:
                record['full_name'] = s['full_name']

            photos.append(record)

        output['comments'] = photos

        sql = "SELECT " + ProtectiveSecurityData.psp_survey_saa_star() + " FROM psp_survey_saa "
        sql += " WHERE survey_id = " + str(org_id) + " and section_id = " + str(section_id)

        rs = SqlData.sql(sql)
        photos = []

        for record in rs:
            sql = "SELECT * FROM nua_user WHERE id = " + record['user_id']
            s = SqlData.sql0(sql)
            if s is None:
                record['full_name'] = "Not Found"
            else:
                record['full_name'] = s['full_name']

            photos.append(record)

        output['saa'] = photos

        try:
            sql = "SELECT id FROM psp_survey_background WHERE survey_id = " + str(org_id)
            rs = SqlData.sql0(sql)
            if rs is None:
                post = {"table_name": "psp_survey_background", "action": "insert"}
                post['survey_id'] = org_id
                post['user_id'] = data['uid']
                post['school_name'] = org['org_name']
                post['mailing_address'] = org['mailing_address']
                post['delivery_address'] = org['delivery_address']
                post['city'] = org['city']
                post['state'] = org['state']
                post['zip'] = org['zip']
                post['school_administrator_name'] = org['administrator_name']
                SqlData.post(post)
        except:
            return {"XXX": "XXX"}

        sql = "SELECT * FROM psp_survey_background WHERE survey_id = " + str(org_id)
        rs = SqlData.sql0(sql)
        output['formData'] = rs

        return output

    @staticmethod
    def get_survey_section_background_new(data):

        sql = "select * from nua_user where id = " + str(data['uid'])
        r = SqlData.sql0(sql)

        org_id = r['org_id']

        sql = "select " + ProtectiveSecurityData.doc_organization_star() + " from "
        sql += "doc_organization where id = " + str(org_id)

        org = SqlData.sql0(sql)

        output = {"org": org}

        section_id = data['data']['section_id']
        sql = "SELECT " + ProtectiveSecurityData.psp_saa_type_star() + " FROM psp_saa_type "
        sql += " WHERE section = " + str(section_id)
        sql += " order by options"
        rs = SqlData.sql(sql)

        output['saa_types'] = rs

        sql = "SELECT * FROM psp_survey_participant WHERE survey_id = " + str(org_id)
        rs = SqlData.sql(sql)
        output['participants'] = rs

        saa_form_data = {"section_id": section_id, "survey_id": org_id}

        sql = "SELECT id, saa_question FROM psp_saa_type WHERE section = " + str(section_id)
        sql += " and saa_question <> '' order by ssa_order"
        rs = SqlData.sql(sql)

        for record in rs:
            sql = "SELECT " + ProtectiveSecurityData.psp_survey_saa_star() + " from psp_survey_saa "
            sql += " where survey_id = " + str(org_id) + " and saa_type = " + str(record['id'])
            r = SqlData.sql0(sql)
            idx = 'p' + str(record['id'])
            if r is None:
                saa_form_data[idx] = ""
            else:
                saa_form_data[idx] = "Y"

        output['saaFormData'] = saa_form_data
        output['saa_options'] = rs

        sql = "SELECT * FROM psp_photo_type WHERE section = " + str(section_id)
        sql += " order by options"
        rs = SqlData.sql(sql)
        output['photo_types'] = rs

        sql = "SELECT * FROM psp_document_type WHERE section = " + str(section_id)
        sql += " order by options"
        rs = SqlData.sql(sql)
        output['document_types'] = rs

        sql = "SELECT * FROM psp_survey_photo WHERE survey_id = " + str(org_id)
        sql += " and section_id = " + str(section_id)
        rs = SqlData.sql(sql)

        photos = []
        for record in rs:
            if record['photo_type'] == '':
                record['photo_type'] = '0'
            sql = "select full_name from nua_user where id = " + str(record['user_id'])
            m = SqlData.sql0(sql)
            if m is None:
                record['user_name'] = 'Not found'
            else:
                record['user_name'] = m['full_name']

            sql = "select options from psp_photo_type where id = " + str(record['photo_type'])
            m = SqlData.sql0(sql)
            if m is None:
                record['type_name'] = ''
            else:
                record['type_name'] = m['options']

            photos.append(record)

        output['photos'] = photos

        sql = "SELECT * FROM psp_survey_document WHERE survey_id = " + str(org_id)
        sql += " and section_id = " + str(section_id)

        rs = SqlData.sql(sql)

        photos = []

        for record in rs:
            sql = "select options from psp_document_type where id = " + str(record['document_type'])
            s = SqlData.sql0(sql)
            if s is None:
                record['type_name'] = ""
            else:
                record['type_name'] = s['options']

            sql = "SELECT * FROM nua_user WHERE id = " + str(record['user_id'])
            s = SqlData.sql0(sql)
            if s is None:
                record['full_name'] = "Not Found"
            else:
                record['full_name'] = s['full_name']

            photos.append(record)

        output['documents'] = photos

        sql = "SELECT * FROM psp_survey_comment WHERE option_id = 0 and asset_id = 0 and survey_id = " + str(org_id)
        sql += " and section_id = " + str(section_id)
        rs = SqlData.sql(sql)
        photos = []

        for record in rs:
            sql = "SELECT * FROM nua_user WHERE id = " + str(record['user_id'])
            s = SqlData.sql0(sql)
            if s is None:
                record['full_name'] = "Not Found"
            else:
                record['full_name'] = s['full_name']

            photos.append(record)

        output['comments'] = photos

        sql = "SELECT " + ProtectiveSecurityData.psp_survey_saa_star() + " FROM psp_survey_saa "
        sql += " WHERE survey_id = " + str(org_id) + " and section_id = " + str(section_id)

        rs = SqlData.sql(sql)
        photos = []

        for record in rs:
            sql = "SELECT * FROM nua_user WHERE id = " + str(record['user_id'])
            s = SqlData.sql0(sql)
            if s is None:
                record['full_name'] = "Not Found"
            else:
                record['full_name'] = s['full_name']

            photos.append(record)

        output['saa'] = photos

        try:
            sql = "SELECT id FROM psp_survey_background WHERE survey_id = " + str(org_id)
            rs = SqlData.sql0(sql)
            if rs is None:
                post = {"table_name": "psp_survey_background", "action": "insert"}
                post['survey_id'] = org_id
                post['user_id'] = data['uid']
                post['school_name'] = org['org_name']
                post['mailing_address'] = org['mailing_address']
                post['delivery_address'] = org['delivery_address']
                post['city'] = org['city']
                post['state'] = org['state']
                post['zip'] = org['zip']
                post['school_administrator_name'] = org['administrator_name']
                SqlData.post(post)
        except:
            return {"XXX": "XXX"}

        sql = "SELECT * FROM psp_survey_background WHERE survey_id = " + str(org_id)
        rs = SqlData.sql0(sql)
        output['formData'] = rs

        sql = "SELECT " + ProtectiveSecurityData.psp_section_template_star() + " FROM psp_template_section WHERE id = " + str(section_id)
        out = SqlData.sql0(sql)
        out['data'] = output

        return out

    @staticmethod
    def post_saa_option_change(data):
        uid = data['uid']
        d = data['data']
        section_id = d['section_id']
        survey_id = d['survey_id']
        for name, value in d.items():
            if name != 'section_id' and name != 'survey_id':
                i = name.replace("p", "")
                if value == 'Y':
                    sql = "select id from psp_survey_saa where survey_id = "
                    sql += str(survey_id) + " and saa_type = '" + str(i) + "'"
                    t = SqlData.sql0(sql)
                    if t is None:
                        sql = "select options from psp_saa_type where id = " + i
                        yy = SqlData.sql0(sql)

                        post = {"table_name": "psp_survey_saa", "action": "insert"}
                        post['survey_id'] = survey_id
                        post['section_id'] = section_id
                        post['saa_name'] = yy['options']
                        post['saa_type'] = i
                        post['user_id'] = uid
                        post['system_gen'] = 'Y'
                        SqlData.post(post)
                else:
                    sql = "delete from psp_survey_saa where survey_id = " + str(survey_id)
                    sql += " and saa_type = '" + i + "' and system_gen = 'Y'"
                    SqlData.execute(sql)

        output = {"error_code": "0"}
        return output

    @staticmethod
    def push_option(options, survey_id, question_id):
        sql = "select * from psp_template_option WHERE option_id = " + str(question_id)
        o = SqlData.sql0(sql)
        o['selected'] = 'N'

        # return options
        sql = "select value, text from psp_survey_option WHERE option_id = " + str(question_id)
        sql += " AND org_id = " + str(survey_id)

        rs = SqlData.sql0(sql)
        if rs is None:
            if o['option_type'] != 'Radio Group' and o['option_type'] != 'Checkbox Group':
                options['p' + str(question_id)] = ""
            else:
                options['p' + str(question_id)] = ""
        else:
            if o['option_type'] != 'Radio Group' and o['option_type'] != 'Checkbox Group':
                options['p' + str(question_id)] = rs['value']
            else:
                options['p' + str(question_id)] = rs['value']

        return options

    @staticmethod
    def post_survey_change(data):
        formData = data['data']['formData']
        org_id = formData['survey_id']

        for name, value in formData.items():
            if name != 'option_id' and name != 'survey_id' and name != "question_id":
                oid = name.replace('p', "")

                sql = "select " + ProtectiveSecurityData.psp_template_option_star() + " from psp_template_option where option_id = " + str(oid)
                r = SqlData.sql0(sql)

                option_type = r['option_type']
                if option_type != "Radio Group" and option_type != "Radio Button":

                    if value == 'N' or value == '':
                        sql = "delete from psp_survey_option where "
                        sql += " org_id = " + str(org_id) + " and option_id = " + str(oid)
                        SqlData.execute(sql)
                    else:
                        sql = "select id from psp_survey_option where "
                        sql += " org_id = " + str(org_id) + " and option_id = " + str(oid)
                        rs = SqlData.sql0(sql)

                        post = {"table_name": "psp_survey_option", "action": "insert" }
                        post['org_id'] = str(org_id)
                        post['option_id'] = str(oid)
                        post['value'] = formData['p' + str(oid)]
                        if rs is not None:
                            post['id'] = rs['id']
                        SqlData.post(post)
                else:
                    if option_type == 'Radio Group':
                        sql = "select * from psp_survey_option where org_id = " + str(org_id) + " and "
                        sql += "option_id = " + str(oid)
                        rs = SqlData.sql0(sql)
                        post = {"table_name": "psp_survey_option", "action": "insert"}
                        post['org_id'] = str(org_id)
                        post['option_id'] = str(oid)
                        post['value'] = formData['p' + str(oid)]
                        if rs is not None:
                            post['id'] = rs['id']
                        SqlData.post(post)

                        sql = "select * from psp_survey_option where org_id = " + str(org_id) + " and "
                        sql += " option_id = " + str(value)
                        rs = SqlData.sql0(sql)

                        post = {"table_name": "psp_survey_option", "action": "insert"}
                        post['org_id'] = str(org_id)
                        post['option_id'] = str(oid)
                        post['value'] = 'Y'
                        if rs is not None:
                            post['id'] = rs['id']
                        SqlData.post(post)

                        sql = "select * from psp_template_option where option_group = " + str(oid)
                        r = SqlData.sql(sql)
                        for s in r:
                            sql = "delete from psp_survey_option where "
                            sql += " option_id = " + str(s['option_id']) + " and option_id <> " + str(value)
                            SqlData.execute(sql)
        output = {"error_code": 0}
        return output
    @staticmethod
    def get_survey_questions(data):
        output = {}
        i = data['data']['question_id']

        sql = "select org_id from nua_user where id = " + str(data['uid'])
        r = SqlData.sql0(sql)

        survey_id = r['org_id']

        formData = {"question_id": i, "survey_id": survey_id}

        conditionals = {}

        sql = "SELECT " + ProtectiveSecurityData.psp_template_option_star() + " FROM "
        sql += " psp_template_option WHERE option_id = " + str(i)
        rs = SqlData.sql0(sql)

        output['question'] = rs
        section_id = rs['section_id']


        sql = "SELECT * FROM psp_survey_comment WHERE option_id = " + str(i)
        sql += " and asset_id = 0"

        rs = SqlData.sql(sql)

        output['comments'] = rs

        if rs is not None:
            commentData = rs
        else:
            commentData = {"id": 0}
            commentData['survey_id'] = 0
            commentData['template_id'] = 0
            commentData['option_id'] = i
            commentData['section_id'] = 0
            commentData['asset_id'] = 0
            commentData['order_id'] = 0
            commentData['text'] = ""
            commentData['comment_type'] = ""
            commentData['user_id'] = data['uid']

        output['commentData'] = commentData

        formData = ProtectiveSecurity.push_option(formData, survey_id, i)

        output['question']['model'] = 'p' + str(i)

        sql = "SELECT id, option_id, section_id, parent_id,  cast(option_type as varchar(80)) as option_type, "
        sql += " cast(option_text as varchar(200)) as option_text, section_id, "
        sql += " option_id, option_group, option_order FROM psp_template_option WHERE "
        sql += " option_group = " + str(i)
        sql += " and section_id = " + str(section_id)
        sql += " ORDER BY option_order"

        rs2 = SqlData.sql(sql)

        boilerplate = []
        options = []

        for r in rs2:
            if r['option_type'] == 'Checkbox':
                r['model'] = 'p' + str(r['parent_id'])
                boilerplate.append(r)
                formData = ProtectiveSecurity.push_option(formData, survey_id, r['option_id'])
            if r['option_type'] == 'Checkbox Button':
                formData = ProtectiveSecurity.push_option(formData, survey_id, r['option_id'])
            if r['option_type'] == 'Radio Button':
                formData = ProtectiveSecurity.push_option(formData, survey_id, r['option_id'])
            if r['option_type'] == 'Text':
                formData = ProtectiveSecurity.push_option(formData, survey_id, r['option_id'])
            if r['option_type'] == 'Textarea':
                formData = ProtectiveSecurity.push_option(formData, survey_id, r['option_id'])
            if r['option_type'] == 'Date':
                formData = ProtectiveSecurity.push_option(formData, survey_id, r['option_id'])
            options.append(r)

        output['options'] = options

        sql = "SELECT id, option_id, section_id, parent_id, "
        sql += " cast(option_text as varchar(200)) as option_text, cast(option_type as varchar(80)) as option_type, "
        sql += " option_group, option_order FROM psp_template_option WHERE "
        sql += " option_group = " + str(i)
        sql += " and section_id = " + str(section_id)
        sql += " ORDER BY option_order"

        rs2 = SqlData.sql(sql)
        for rr in rs2:
            sql = "SELECT id, option_id, section_id, parent_id, "
            sql += " cast(option_text as varchar(200)) as option_text, "
            sql += " cast(option_type as varchar(80)) as option_type, "
            sql += " option_order, option_group FROM psp_template_option WHERE "
            sql += " parent_id = " + str(rr['option_id'])
            sql += " AND section_id = " + str(section_id)
            sql += " and option_group = 0 ORDER BY option_order"

            rs3 = SqlData.sql(sql)

            for r in rs3:
                r['model'] = 'p' + str(r['parent_id'])
                boilerplate.append(r)

        output['boilerplate'] = boilerplate

        sql = "SELECT id, option_id, section_id, parent_id, "
        sql += "cast(option_text as varchar(200)) as option_text, "
        sql += " cast(option_type as varchar(80)) as option_type "
        sql += " FROM psp_template_option WHERE "
        sql += " option_group = " + str(i)
        sql += " ORDER BY option_order"

        rs2 = SqlData.sql(sql)
        options = []

        for r in rs2:
            sql = "SELECT id, option_id, section_id, parent_id, "
            sql += " cast(option_text as varchar(200)) as option_text, "
            sql += " cast(option_type as varchar(80)) as option_type, "
            sql += " option_order FROM psp_template_option WHERE "
            sql += " parent_id = " + str(r['option_id'])
            sql += " AND option_group = 0 ORDER BY option_order"

            rs2 = SqlData.sql(sql)

            if len(rs2) > 0:
                options.append(r)

                sql = "select cast(text as varchar(200)) as text from psp_survey_option "
                sql += " WHERE option_id = " + str(r['option_id'])
                sql += " AND org_id = " + str(survey_id)

                rs = SqlData.sql(sql)

                if len(rs) == 0:
                    conditionals['p' + str(r['option_id'])] = 'Y'
                else:
                    conditionals['p' + str(r['option_id'])] = 'N'

        conditionals['p' + str(i)] = formData['p' + str(i)]
        output['formData'] = formData
        output['conditionals'] = conditionals

        return output
