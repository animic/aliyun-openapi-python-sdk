# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class GetTaskListFilterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'devops-rdc', '2020-03-03', 'GetTaskListFilter')
		self.set_method('POST')

	def get_InvolveMembers(self):
		return self.get_body_params().get('InvolveMembers')

	def set_InvolveMembers(self,InvolveMembers):
		self.add_body_params('InvolveMembers', InvolveMembers)

	def get_ExecutorId(self):
		return self.get_body_params().get('ExecutorId')

	def set_ExecutorId(self,ExecutorId):
		self.add_body_params('ExecutorId', ExecutorId)

	def get_OrderCondition(self):
		return self.get_body_params().get('OrderCondition')

	def set_OrderCondition(self,OrderCondition):
		self.add_body_params('OrderCondition', OrderCondition)

	def get_SprintId(self):
		return self.get_body_params().get('SprintId')

	def set_SprintId(self,SprintId):
		self.add_body_params('SprintId', SprintId)

	def get_Extra(self):
		return self.get_body_params().get('Extra')

	def set_Extra(self,Extra):
		self.add_body_params('Extra', Extra)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_ScenarioFieldConfigId(self):
		return self.get_body_params().get('ScenarioFieldConfigId')

	def set_ScenarioFieldConfigId(self,ScenarioFieldConfigId):
		self.add_body_params('ScenarioFieldConfigId', ScenarioFieldConfigId)

	def get_IsDone(self):
		return self.get_body_params().get('IsDone')

	def set_IsDone(self,IsDone):
		self.add_body_params('IsDone', IsDone)

	def get_ObjectType(self):
		return self.get_body_params().get('ObjectType')

	def set_ObjectType(self,ObjectType):
		self.add_body_params('ObjectType', ObjectType)

	def get_ProjectId(self):
		return self.get_body_params().get('ProjectId')

	def set_ProjectId(self,ProjectId):
		self.add_body_params('ProjectId', ProjectId)

	def get_PageToken(self):
		return self.get_body_params().get('PageToken')

	def set_PageToken(self,PageToken):
		self.add_body_params('PageToken', PageToken)

	def get_Order(self):
		return self.get_body_params().get('Order')

	def set_Order(self,Order):
		self.add_body_params('Order', Order)

	def get_TagId(self):
		return self.get_body_params().get('TagId')

	def set_TagId(self,TagId):
		self.add_body_params('TagId', TagId)

	def get_TaskFlowStatusId(self):
		return self.get_body_params().get('TaskFlowStatusId')

	def set_TaskFlowStatusId(self,TaskFlowStatusId):
		self.add_body_params('TaskFlowStatusId', TaskFlowStatusId)

	def get_DueDateStart(self):
		return self.get_body_params().get('DueDateStart')

	def set_DueDateStart(self,DueDateStart):
		self.add_body_params('DueDateStart', DueDateStart)

	def get_CreatorId(self):
		return self.get_body_params().get('CreatorId')

	def set_CreatorId(self,CreatorId):
		self.add_body_params('CreatorId', CreatorId)

	def get_Priority(self):
		return self.get_body_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_body_params('Priority', Priority)

	def get_DueDateEnd(self):
		return self.get_body_params().get('DueDateEnd')

	def set_DueDateEnd(self,DueDateEnd):
		self.add_body_params('DueDateEnd', DueDateEnd)

	def get_OrgId(self):
		return self.get_body_params().get('OrgId')

	def set_OrgId(self,OrgId):
		self.add_body_params('OrgId', OrgId)

	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)