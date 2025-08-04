from enum import Enum


class V1draftSupplyCreateStatus(str, Enum):

    DRAFTSUPPLYCREATESTATUSUNKNOWN = "DraftSupplyCreateStatusUnknown"
    DRAFTSUPPLYCREATESTATUSSUCCESS = "DraftSupplyCreateStatusSuccess"
    DRAFTSUPPLYCREATESTATUSFAILED = "DraftSupplyCreateStatusFailed"
    DRAFTSUPPLYCREATESTATUSINPROGRESS = "DraftSupplyCreateStatusInProgress"
