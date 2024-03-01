from odoo import fields, models


class HrJob(models.Model):
    _inherit = "hr.job"

    def _compute_to_recruit(self):
        contract_obj = self.env["hr.contract"]
        for rec in self:
            rec.to_recruit = contract_obj.search_count(
                [("job_id", "=", rec.id), ("state", "=", "open")]
            )
            if (rec.no_of_recruitment - rec.to_recruit) > 0:
                rec.website_published = True
            else:
                rec.website_published = False

    to_recruit = fields.Integer(string="To be recruited", compute="_compute_to_recruit")
