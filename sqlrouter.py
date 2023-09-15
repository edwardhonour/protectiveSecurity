import json
import mysql.connector
from fastapi import FastAPI, Request, Response
from sqldata import *
from protectivesecurity import *
from sqlauth import *
import logging


class Router(SqlData):

    def __init__(self):
        super().__init__()

    @staticmethod
    def test(post_data):
        logging.info(post_data)
        if 'q' not in post_data:
            post_data['q'] = "user"

        # if post_data is from Angular Resolver, split the parameters.

        aa = post_data['q'].split("/")
        if aa[0] == '':
            post_data['q'] = aa[1]
            if len(aa) > 2:
                post_data['id'] = aa[2]
            if len(aa) > 3:
                post_data['id2'] = aa[3]
            if len(aa) > 4:
                post_data['id3'] = aa[4]
        else:
            post_data['q'] = aa[0]

        # process data
        if post_data['q'] == 'sadmin':
            return SqlAuth.create_user('edward@gmail.com', 'Loipol229!')
        elif post_data['q'] == 'get-survey-main-menu':
            return ProtectiveSecurity.get_survey_main_menu(post_data)
        elif post_data['q'] == 'survey':
            return ProtectiveSecurity.get_survey_home(post_data)
        elif post_data['q'] == 'get-survey-section':
            return ProtectiveSecurity.get_survey_section(post_data)
        elif post_data['q'] == 'get-survey-section-background':
            return ProtectiveSecurity.get_survey_section_background(post_data)
        elif post_data['q'] == 'get-survey-section-background-new':
            return ProtectiveSecurity.get_survey_section_background_new(post_data)
        elif post_data['q'] == 'post-saa-option-change':
            return ProtectiveSecurity.post_saa_option_change(post_data)
        elif post_data['q'] == 'get-survey-question':
            return ProtectiveSecurity.get_survey_questions(post_data)
        elif post_data['q'] == 'get-survey-asset-section':
            return ProtectiveSecurity.get_survey_asset_section(post_data)
        elif post_data['q'] == 'post-survey-change':
            return ProtectiveSecurity.post_survey_change(post_data)
        elif post_data['q'] == 'post-facility-form':
            pass
            # output =# A->postFacilityForm(# data);
        elif post_data['q'] == 'post-section-comment':
            pass
            # output =# A->postSectionComment(# data);
        elif post_data['q'] == 'post-section-saa':
            pass
            # output =# A->postSectionSAA(# data);
        elif post_data['q'] == 'get-stakeholder-form':
            pass
            # output =# A->getStakeholderForm(# data);
        elif post_data['q'] == 'get-facility-form':
            pass
            # output =# A->getFacilityForm(# data);
        elif post_data['q'] == 'add-option':
            pass
            # output =# A->addOption(# data);
        elif post_data['q'] == 'post-form-option':
            pass
            # output =# A->addFormOption(# data);
        elif post_data['q'] == 'post-base-question':
            pass
            # output =# A->addBaseQuestion(# data);
        elif post_data['q'] == 'add-template':
            pass
            # output =# A->addTemplate(# data);
        elif post_data['q'] == 'delete-template':
            pass
            # output =# A->deleteTemplate(# data);
        elif post_data['q'] == 'add-template-section':
            pass
            # output =# A->addTemplateSection(# data);
        elif post_data['q'] == 'get-survey-asset-section':
            pass
            # output =# A->getAssetSurveySection(# data);
        elif post_data['q'] == 'get-survey-question':
            pass
            # output =# A->getSurveyQuestion(# data);
        elif post_data['q'] == 'get-asset-survey-question':
            pass
            # output =# A->getAssetSurveyQuestion(# data);
        elif post_data['q'] == 'templates':
            pass
        elif post_data['q'] == 'template-list':
            pass
        elif post_data['q'] == 'preview-list':
            pass
        elif post_data['q'] == 'workspace-dashboard':
            pass
            # output =# A->getProjectDashboard(# data);
        elif post_data['q'] == 'survey':
            pass
            # output =# A->getAssessmentDashboard(# data);
        elif post_data['q'] == 'post-participant':
            pass
            # output =# A->postParticipant(# data);
        elif post_data['q'] == 'preview-section':
            pass
            # output =# A->getSurveyPreviewSection(# data);
        elif post_data['q'] == 'template-dashboard':
            pass
            # output =# A->getTemplateDashboard(# data);
        elif post_data['q'] == 'template-section-dashboard':
            pass
            # output =# A->getTemplateSectionDashboard(# data);
        elif post_data['q'] == 'get-one-option':
            pass
            # output=# A->getOneOption(# data);
        elif post_data['q'] == 'document-dashboard':
            pass
            # output=# A->getDocumentDashboard(# data);
        elif post_data['q'] == 'org-dashboard':
            pass
            # output=# A->getOrgDashboard(# data);
        elif post_data['q'] == 'get-one-form-option':
            pass
            # output=# A->getOneFormOption(# data);
        elif post_data['q'] == 'post-form-option':
            pass
            # output=# A->addFormOption(# data);
        elif post_data['q'] == 'post-stakeholder-form':
            pass
            # output=# A->postStakeholderForm(# data);
        elif post_data['q'] == 'preview-section':
            pass
            # output=# A->previewSection(# data);
        elif post_data['q'] == 'stakeholder-list':
            pass
            # output=# A->getStakeholderList(# data);
        elif post_data['q'] == 'stakeholders':
            pass
            # output=# A->getStakeholderList(# data);
        elif post_data['q'] == 'stakeholder-dashboard':
            pass
            # output=# A->getStakeholderDashboard(# data);
        elif post_data['q'] == 'facilities':
            pass
            # output=# A->getFacilityList(# data);
        elif post_data['q'] == 'facility-dashboard':
            pass
            # output=# A->getFacilityDashboard(# data);
        elif post_data['q'] == 'surveys':
            pass
            # output=# A->getSurveyList(# data);
        elif post_data['q'] == 'survey-dashboard':
            pass
            # output=# A->getFacilityDashboard(# data);
        elif post_data['q'] == 'get-template-list':
            pass
            # output=# A->getSurveyTemplates(# data);
        elif post_data['q'] == 'previews':
            pass
            # output =# A->getSurveyTemplates(# data);
        elif post_data['q'] == 'sadmin':
            pass
            # output =# A->getAdminDashboard(# data);
        elif post_data['q'] == 'get-schedule-form':
            pass
            # output =# A->getScheduleForm(# data);
        elif post_data['q'] == 'post-schedule-form':
            pass
            # output =# A->postScheduleForm(# data);
        elif post_data['q'] == 'get-facility-assessments':
            pass
            # output =# A->getFacilityAssessments(# data);
        elif post_data['q'] == 'assessments':
            pass
            # output =# A->getAssessments(# data);
        elif post_data['q'] == 'get-facility-preview-info':
            pass
            # output =# A->getFacilityPreviewInfo(# data);
        elif post_data['q'] == 'get-saa-form':
            pass
            # output =# A->getFacilityPreviewInfo(# data);
        elif post_data['q'] == 'get-tenant-form':
            pass
            # output =# A->getTenantForm(# data);
        elif post_data['q'] == 'get-assessment-record':
            pass
            # output =# A->getAssessmentRecord(# data);
        elif post_data['q'] == 'assessment-dashboard':
            pass
            # output =# A->getAssessmentDashboard(# data);
        elif post_data['q'] == 'get-assessment-section':
            pass
            # output =# A->getAssessmentSection(# data);
        elif post_data['q'] == 'delete-template-section':
            pass
            # output =# A->deleteTemplateSection(# data);
        elif post_data['q'] == 'settings':
            pass
            # output =# A->getSettings(# data);
        elif post_data['q'] == 'make-org-workspace':
            pass
            # output =# A->makeOrgWorkspace(# data);
        elif post_data['q'] == 'ocuments':
            pass
            # output =# A->getDocumentList(# data);
        elif post_data['q'] == 'team':
            pass
            # output =# A->getTeamList(# data);
        elif post_data['q'] == 'shares':
            pass
            # output =# A->getShareList(# data);
        elif post_data['q'] == 'orgs':
            pass
            # output =# A->getOrgList(# data);
        elif post_data['q'] == 'update-doc-metadata':
            pass
            # output =# A->updateDoc(# data);
        elif post_data['q'] == 'get-survey-section-background':
            pass
            # output =# A->getSurveySectionBackground(# data);
        elif post_data['q'] == 'get-survey-section-background-new':
            pass
            # output =# A->getSurveySectionBackgroundNew(# data);
        elif post_data['q'] == 'post-update-photo':
            pass
            # output =# A->postUpdatePhoto(# data);
        elif post_data['q'] == 'post-update-document':
            pass
            # output =# A->postUpdateDocument(# data);
        elif post_data['q'] == 'post-survey-change':
            pass
            # output =# A->postSurveyChange(# data);
        elif post_data['q'] == 'post-asset-survey-change':
            pass
            # output =# A->postAssetSurveyChange(# data);
        elif post_data['q'] == 'post-general-description':
            pass
            # output =# A->postGeneralDescription(# data);
        elif post_data['q'] == 'photos':
            pass
            # output =# A->pspPhotoList(# data);
        elif post_data['q'] == 'comments':
            pass
            # output =# A->pspCommentList(# data);
        elif post_data['q'] == 'documents':
            pass
            # output =# A->pspDocumentList(# data);
        elif post_data['q'] == post_data['q'] == 'do-something':
            return {"result": post_data['q']}
        else:
            return {"result": "nothing"}

