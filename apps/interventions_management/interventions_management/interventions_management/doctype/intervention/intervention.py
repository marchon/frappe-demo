# -*- coding: utf-8 -*-
# Copyright (c) 2015, Anybox and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class intervention(Document):

    def validate(self):
        if frappe.session.user:
            self.author = frappe.session.user
        else:
            frappe.throw(_("Intervention needs an author"))

