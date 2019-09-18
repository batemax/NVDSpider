# -*- coding: utf-8 -*-
# 从json读取数据，并存储到数据库中
from datetime import datetime
from urllib.parse import urljoin

import pymongo
import os
import json
from NVDSpider.settings import MONGO_HOST
from NVDSpider.settings import MONGO_PORT
from NVDSpider.settings import MONGO_DB
from NVDSpider.settings import MONGO_VULN


class mongoSync(object):
    def __init__(self):
        self.client = pymongo.MongoClient(MONGO_HOST,MONGO_PORT)
        self.db = self.client[MONGO_DB]  # 获得数据库的句柄
        self.coll = self.db[MONGO_VULN]  # 获得collection的句柄
        # self.list = []

    def loadFile(self,path):
        files = os.listdir(path)
        for file in files:
            if not os.path.isdir(file):
                file = path + file
                # self.list.append(file)
                self.sync(file)

    def sync(self,file):
        with open(file,'rb') as f:
            data = json.load(f)
            cve_items = data["CVE_Items"]
            for cve_item in cve_items:
                cve_info = cve_item['cve']
                item_dict = {}
                # cve_id
                cve_id = cve_info['CVE_data_meta']['ID']
                cve_url = urljoin('https://nvd.nist.gov/vuln/detail/', cve_id)
                publishDate = cve_item['publishedDate']
                publishDate = datetime.strptime(publishDate, "%Y-%m-%dT%H:%MZ")
                modifyDate = cve_item['lastModifiedDate']
                modifyDate = datetime.strptime(modifyDate, "%Y-%m-%dT%H:%MZ")

                item_dict['_id'] = cve_id
                item_dict['vuln_url'] = cve_url
                item_dict['rel_time'] = publishDate
                item_dict['upd_time'] = modifyDate

                # 判断v2信息是否存在
                try:
                    cve_impact_v2 = cve_item['impact']['baseMetricV2']
                except:
                    print(cve_id+"没有V2信息")
                    self.coll.update({'_id': cve_id}, {'$set': item_dict}, upsert=True)
                else:
                    v2_vector = cve_impact_v2['cvssV2']['vectorString']
                    v2_accessVector = cve_impact_v2['cvssV2']['accessVector']
                    v2_accessComplexity = cve_impact_v2['cvssV2']['accessComplexity']
                    v2_authentication = cve_impact_v2['cvssV2']['authentication']
                    v2_confidentialityImpact = cve_impact_v2['cvssV2']['confidentialityImpact']
                    v2_integrityImpact = cve_impact_v2['cvssV2']['integrityImpact']
                    v2_availabilityImpact = cve_impact_v2['cvssV2']['availabilityImpact']
                    v2_baseScore = cve_impact_v2['cvssV2']['baseScore']
                    v2_severity = cve_impact_v2['severity']
                    v2_exploitabilityScore = cve_impact_v2['exploitabilityScore']
                    v2_impactScore = cve_impact_v2['impactScore']

                    item_dict['v2_vector'] = v2_vector
                    item_dict['v2_AV'] = v2_accessVector
                    item_dict['v2_AC'] = v2_accessComplexity
                    item_dict['v2_AU'] = v2_authentication
                    item_dict['v2_C'] = v2_confidentialityImpact
                    item_dict['v2_I'] = v2_integrityImpact
                    item_dict['v2_A'] = v2_availabilityImpact
                    item_dict['v2_base_score'] = v2_baseScore
                    item_dict['v2_severity'] = v2_severity
                    item_dict['v2_exp_score'] = v2_exploitabilityScore
                    item_dict['v2_impact_score'] = v2_impactScore

                    # 判断v3信息是否存在
                    try:
                        cve_impact_v3 = cve_item['impact']['baseMetricV3']
                    except:
                        print(cve_id+"没有V3信息")
                    else:
                        v3_vector = cve_impact_v3['cvssV3']['vectorString']
                        v3_attackVector = cve_impact_v3['cvssV3']['attackVector']
                        v3_attackComplexity = cve_impact_v3['cvssV3']['attackComplexity']
                        v3_privilegesRequired = cve_impact_v3['cvssV3']['privilegesRequired']
                        v3_userInteraction = cve_impact_v3['cvssV3']['userInteraction']
                        v3_scope = cve_impact_v3['cvssV3']['scope']
                        v3_confidentialityImpact = cve_impact_v3['cvssV3']['confidentialityImpact']
                        v3_integrityImpact = cve_impact_v3['cvssV3']['integrityImpact']
                        v3_availabilityImpact = cve_impact_v3['cvssV3']['availabilityImpact']
                        v3_baseScore = cve_impact_v3['cvssV3']['baseScore']
                        v3_baseSeverity = cve_impact_v3['cvssV3']['baseSeverity']
                        v3_exploitabilityScore = cve_impact_v3['exploitabilityScore']
                        v3_impactScore = cve_impact_v3['impactScore']

                        item_dict['v3_vector'] = v3_vector
                        item_dict['v3_AV'] = v3_attackVector
                        item_dict['v3_AC'] = v3_attackComplexity
                        item_dict['v3_PR'] = v3_privilegesRequired
                        item_dict['v3_UI'] = v3_userInteraction
                        item_dict['v3_S'] = v3_scope
                        item_dict['v3_C'] = v3_confidentialityImpact
                        item_dict['v3_I'] = v3_integrityImpact
                        item_dict['v3_A'] = v3_availabilityImpact
                        item_dict['v3_base_score'] = v3_baseScore
                        item_dict['v3_vuln_level'] = v3_baseSeverity
                        item_dict['v3_exp_score'] = v3_exploitabilityScore
                        item_dict['v3_impact_score'] = v3_impactScore
                    finally:
                        # 计算
                        description = cve_info['description']['description_data'][0]['value']

                        vuln_ref = []
                        for data in cve_info['references']['reference_data']:
                            ref_data = {}
                            ref_url = data['url']
                            ref_tags = data['tags']
                            # ref_tags = []
                            # for tag in data['tags']:
                            #     ref_tags.append(tag)
                            ref_data['ref_url'] = ref_url
                            ref_data['ref_tags'] = ref_tags
                            vuln_ref.append(ref_data)
                        item_dict['vuln_ref'] = vuln_ref

                        problem_type = cve_info['problemtype']['problemtype_data'][0]
                        cwe_type = []
                        descs = problem_type['description']
                        for desc in descs:
                            cwe_type.append(desc['value'])

                        item_dict['vuln_desc'] = description
                        item_dict['vuln_type'] = cwe_type
                        # 插入数据库
                        self.coll.update({'_id': cve_id}, {'$set': item_dict}, upsert=True)
        self.client.close()