"""
Models the proteome (non-pride) object.
"""

import json
import logging
import os
import string
from cutlass.iHMPSession import iHMPSession
from cutlass.Base import Base
from cutlass.aspera import aspera
from cutlass.Util import *

# pylint: disable=W0703, C1801

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class ProteomeNonPride(Base):
    """
    The class encapsulates iHMP proteome non-pride data. It contains all
    the fields required to save a such an object in OSDF.

    Attributes:

        namespace (str): The namespace this class will use in OSDF.
    """
    namespace = "ihmp"

    aspera_server = "aspera2.ihmpdcc.org"

    def __init__(self, *args, **kwargs):
        """
        Constructor for the ProteomeNonPride class. This initializes the
        fields specific to the class, and inherits from the Base class.

        Args:
            None
        """
        self.logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

        self.logger.addHandler(logging.NullHandler())

        self._id = None
        self._version = None
        self._links = {}
        self._tags = []

        # Required properties
        self._comment = None
        self._data_processing_protocol = None
        self._processing_method = None
        self._study = None
        self._subtype = None
        self._local_other_file = None
        self._local_peak_file = None
        self._local_protmod_file = None
        self._local_raw_file = None

        # Optional properties
        self._analyzer = None
        self._date = None
        self._detector = None
        self._exp_description = None
        self._instrument_name = None
        self._other_url = ['']
        self._peak_url = ['']
        self._private_files = None
        self._protmod_format = None
        self._protmod_url = ['']
        self._protocol_name = None
        self._protocol_steps = None
        self._raw_url = ['']
        self._reference = None
        self._search_engine = None
        self._short_label = None
        self._software = None
        self._source = None
        self._title = None

        super(ProteomeNonPride, self).__init__(*args, **kwargs)

    @property
    def analyzer(self):
        """
        str: Returns the single or multiple component setting of the mass
        analyzer.
        """
        self.logger.debug("In 'analyzer' getter.")

        return self._analyzer

    @analyzer.setter
    @enforce_string
    def analyzer(self, analyzer):
        """
        The setter for single or multiple components of the mass analyzer.

        Args:
            analyzer (str): The single/multiple components of the mass analyzer.

        Returns:
            None
        """
        self.logger.debug("In 'analyzer' setter.")

        self._analyzer = analyzer

    @property
    def comment(self):
        """
        str: A descriptive comment for the proteome.
        """
        self.logger.debug("In 'comment' getter.")

        return self._comment

    @comment.setter
    @enforce_string
    def comment(self, comment):
        """
        The setter for a descriptive comment for the proteome.

        Args:
            comment (str): The comment text.

        Returns:
            None
        """
        self.logger.debug("In 'comment' setter.")

        self._comment = comment

    @property
    def data_processing_protocol(self):
        """
        str: A short description of the data processing protocol followed to
        generate associated data sets.
        """
        self.logger.debug("In 'data_processing_protocol' getter.")

        return self._data_processing_protocol

    @data_processing_protocol.setter
    @enforce_string
    def data_processing_protocol(self, data_processing_protocol):
        """
        The setter for the data processing protocol.

        Args:
            data_processing_protocol (str): a short description of the
            protocol.

        Returns:
            None
        """
        self.logger.debug("In 'data_processing_protocol' setter.")

        self._data_processing_protocol = data_processing_protocol

    @property
    def date(self):
        """
        str: The date on which the data were generated.
        """
        self.logger.debug("In 'date' getter.")

        return self._date

    @date.setter
    @enforce_past_date
    def date(self, date):
        """
        The setter for the date.

        Args:
            date (str): The date on which the data were generated.

        Returns:
            None
        """
        self.logger.debug("In 'date' setter.")

        self._date = date

    @property
    def detector(self):
        """
        str: The detector type used.
        """
        self.logger.debug("In 'detector' getter.")

        return self._detector

    @detector.setter
    @enforce_string
    def detector(self, detector):
        """
        The setter for the detector type used.

        Args:
            detector (str): The detector type used.

        Returns:
            None
        """
        self.logger.debug("In 'detector' setter.")

        self._detector = detector

    @property
    def exp_description(self):
        """
        str: The goals and description of the study.
        """
        self.logger.debug("In 'exp_description' getter.")

        return self._exp_description

    @exp_description.setter
    @enforce_string
    def exp_description(self, exp_description):
        """
        The setter for the goals and description of the study.

        Args:
            exp_description (str): The goals and description of the study.

        Returns:
            None
        """
        self.logger.debug("In 'exp_description' setter.")

        self._exp_description = exp_description

    @property
    def instrument_name(self):
        """
        str: The instrument make, model, significant customizations.
        """
        self.logger.debug("In 'instrument_name' getter.")

        return self._instrument_name

    @instrument_name.setter
    @enforce_string
    def instrument_name(self, instrument_name):
        """
        The descriptive name of the instrument make, model, significant
        customizations.

        Args:
            instrument_name (str): Instrument make, model, etc.

        Returns:
            None
        """
        self.logger.debug("In 'instrument_name' setter.")

        self._instrument_name = instrument_name

    @property
    def local_other_file(self):
        """
        str: Path to the local proteome 'other' file to upload.
        """
        self.logger.debug("In 'local_other_file' getter.")

        return self._local_other_file

    @local_other_file.setter
    @enforce_string
    def local_other_file(self, local_other_file):
        """
        The setter for the local proteome 'other' file.

        Args:
            local_other_file (str): The path to the local 'other' file.

        Returns:
            None
        """
        self.logger.debug("In 'local_other_file' setter.")

        self._local_other_file = local_other_file

    @property
    def local_peak_file(self):
        """
        str: Path to the local proteome 'peak' file to upload.
        """
        self.logger.debug("In 'local_peak_file' getter.")

        return self._local_peak_file

    @local_peak_file.setter
    @enforce_string
    def local_peak_file(self, local_peak_file):
        """
        The setter for the local proteome 'peak' file.

        Args:
            local_peak_file (str): The path to the local 'peak' file.

        Returns:
            None
        """
        self.logger.debug("In 'local_peak_file' setter.")

        self._local_peak_file = local_peak_file

    @property
    def local_protmod_file(self):
        """
        str: Path to the local proteome 'protmod' file to upload.
        """
        self.logger.debug("In 'local_protmod_file' getter.")

        return self._local_protmod_file

    @local_protmod_file.setter
    @enforce_string
    def local_protmod_file(self, local_protmod_file):
        """
        The setter for the local proteome 'protmod' file.

        Args:
            local_protmod_file (str): The path to the local 'protmod' file.

        Returns:
            None
        """
        self.logger.debug("In 'local_protmod_file' setter.")

        self._local_protmod_file = local_protmod_file

    @property
    def local_raw_file(self):
        """
        str: Path to the local proteome 'raw' file to upload.
        """
        self.logger.debug("In 'local_raw_file' getter.")

        return self._local_raw_file

    @local_raw_file.setter
    @enforce_string
    def local_raw_file(self, local_raw_file):
        """
        The setter for the local proteome 'raw' file.

        Args:
            local_raw_file (str): The path to the local 'raw' file.

        Returns:
            None
        """
        self.logger.debug("In 'local_raw_file' setter.")

        self._local_raw_file = local_raw_file

    @property
    def private_files(self):
        """
        bool: Whether this object describes private data that should not
        be uploaded to the DCC. Defaults to false.
        """
        self.logger.debug("In 'private_files' getter.")

        return self._private_files

    @private_files.setter
    @enforce_bool
    def private_files(self, private_files):
        """
        The setter for the private files flag to denote this object
        describes data that should not be uploaded to the DCC.

        Args:
            private_files (bool):

        Returns:
            None
        """
        self.logger.debug("In 'private_files' setter.")

        self._private_files = private_files

    @property
    def processing_method(self):
        """
        str: The description of the default peak processing method.
        """
        self.logger.debug("In 'processing_method' getter.")

        return self._processing_method

    @processing_method.setter
    @enforce_string
    def processing_method(self, processing_method):
        """
        The description of the default peak processing method.

        Args:
            processing_method (str): Default peak processing method.

        Returns:
            None
        """
        self.logger.debug("In 'processing_method' setter.")

        self._processing_method = processing_method

    @property
    def protmod_format(self):
        """
        str: The file format of the protein modifications file.
        """
        self.logger.debug("In 'protmod_format' getter.")

        return self._protmod_format

    @protmod_format.setter
    @enforce_string
    def protmod_format(self, protmod_format):
        """
        The file format of the protein modifications file.

        Args:
            protmod_format (str): File format of the protein modifications file.

        Returns:
            None
        """
        self.logger.debug("In 'protmod_format' setter.")

        self._protmod_format = protmod_format

    @property
    def protocol_name(self):
        """
        str: The protocol name with versioning.
        """
        self.logger.debug("In 'protocol_name' getter.")

        return self._protocol_name

    @protocol_name.setter
    @enforce_string
    def protocol_name(self, protocol_name):
        """
        The protocol name with versioning, ideally pointing to a URL.

        Args:
            protocol_name (str): Protocol title with versioning.

        Returns:
            None
        """
        self.logger.debug("In 'protocol_name' setter.")

        self._protocol_name = protocol_name

    @property
    def protocol_steps(self):
        """
        str: Description of the sample processing steps that have been
        performed.
        """
        self.logger.debug("In 'protocol_steps' getter.")

        return self._protocol_steps

    @protocol_steps.setter
    @enforce_string
    def protocol_steps(self, protocol_steps):
        """
        Description of the sample processing steps that have been performed.

        Args:
            protocol_steps (str): sample processing steps.

        Returns:
            None
        """
        self.logger.debug("In 'protocol_steps' setter.")

        self._protocol_steps = protocol_steps

    @property
    def reference(self):
        """
        str: Link to literature citation.
        """
        self.logger.debug("In 'reference' getter.")

        return self._reference

    @reference.setter
    @enforce_string
    def reference(self, reference):
        """
        Link to literature citation for which this experiment provides
        supporting evidence.

        Args:
            reference (str): links to literature citations.

        Returns:
            None
        """
        self.logger.debug("In 'reference' setter.")

        self._reference = reference

    @property
    def search_engine(self):
        """
        str: Name of the protein search engine used, e.g. Mascot 2.2.1.
        """
        self.logger.debug("In 'search_engine' getter.")

        return self._search_engine

    @search_engine.setter
    @enforce_string
    def search_engine(self, search_engine):
        """
        Name of the protein search engine used, e.g. Mascot 2.2.1.

        Args:
            search_engine (str): search engine name.

        Returns:
            None
        """
        self.logger.debug("In 'search_engine' setter.")

        self._search_engine = search_engine

    @property
    def short_label(self):
        """
        str: Nomenclature used to organize experiments.
        """
        self.logger.debug("In 'short_label' getter.")

        return self._short_label

    @short_label.setter
    @enforce_string
    def short_label(self, short_label):
        """
        Nomenclature used to group/organize experiments in a meaningful way,
        e.g. Control Exp II.

        Args:
            short_label (str): the nomenclature.

        Returns:
            None
        """
        self.logger.debug("In 'short_label' setter.")

        self._short_label = short_label

    @property
    def software(self):
        """
        str: All software used during data acquisition and data processing,
        including the software that produced the peak list, with versions.
        """
        self.logger.debug("In 'software' getter.")

        return self._software

    @software.setter
    @enforce_string
    def software(self, software):
        """
        All software used during data acquisition and data processing,
        including the software that produced the peak list, with versions.

        Args:
            software (str): software used.

        Returns:
            None
        """
        self.logger.debug("In 'software' setter.")

        self._software = software

    @property
    def source(self):
        """
        str: Ion source information.
        """
        self.logger.debug("In 'source' getter.")

        return self._source

    @source.setter
    @enforce_string
    def source(self, source):
        """
        Ion source information.

        Args:
            source (str): ion source information.

        Returns:
            None
        """
        self.logger.debug("In 'source' setter.")

        self._source = source

    @property
    def study(self):
        """
        str: One of the 3 studies that are part of the iHMP.
        """
        self.logger.debug("In 'study' getter.")

        return self._study

    @study.setter
    @enforce_string
    def study(self, study):
        """
        One of the 3 studies that are part of the iHMP.

        Args:
            study (str): One of the 3 studies that are part of the iHMP.

        Returns:
            None
        """
        self.logger.debug("In 'study' setter.")

        studies = ["preg_preterm", "ibd", "prediabetes"]

        if study in studies:
            self._study = study
        else:
            raise Exception("Invalid study.")

    @property
    def subtype(self):
        """
        str: The subytpe of the object: 'host' or 'microbiome'.
        """
        self.logger.debug("In 'subtype' getter.")

        return self._subtype

    @subtype.setter
    @enforce_string
    def subtype(self, subtype):
        """
        Subtype to indicate whether this is for a host or microbiome.

        Args:
            subtype (str): 'host' or 'microbiome'

        Returns:
            None
        """
        self.logger.debug("In 'subtype' setter.")

        subtypes = ["host", "microbiome"]

        if subtype in subtypes:
            self._subtype = subtype
        else:
            raise Exception("Invalid subtype.")

    @property
    def title(self):
        """
        str: The experiment title.
        """
        self.logger.debug("In 'title' getter.")

        return self._title

    @title.setter
    @enforce_string
    def title(self, title):
        """
        The experiment title.

        Args:
            title (str): experiment title.

        Returns:
            None
        """
        self.logger.debug("In 'title' setter.")

        self._title = title

    def validate(self):
        """
        Validates the current object's data/JSON against the current
        schema in the OSDF instance for that specific object. All required
        fields for that specific object must be present.

        Args:
            None

        Returns:
            A list of strings, where each string is the error that the
            validation raised during OSDF validation
        """
        self.logger.debug("In validate.")

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, error_message) = session.get_osdf().validate_node(document)

        problems = []
        if not valid:
            self.logger.info("Validation did not succeed.")
            problems.append(error_message)

        if self._private_files:
            self.logger.info("User specified the files are private.")
        else:
            self.logger.info("Data is NOT private, so check that all local file paths are set.")

            if self._local_other_file is None:
                problems.append("Local 'other' file is not yet set.")
            elif not os.path.isfile(self._local_other_file):
                problems.append("Local 'other' file does not point to an actual file.")

            if self._local_peak_file is None:
                problems.append("Local peak file is not yet set.")
            elif not os.path.isfile(self._local_peak_file):
                problems.append("Local peak file does not point to an actual file.")

            if self._local_protmod_file is None:
                problems.append("Local protmod file is not yet set.")
            elif not os.path.isfile(self._local_protmod_file):
                problems.append("Local protmod file does not point to an actual file.")

            if self._local_raw_file is None:
                problems.append("Local raw file is not yet set.")
            elif not os.path.isfile(self._local_raw_file):
                problems.append("Local raw file does not point to an actual file.")

        if 'derived_from' not in self._links.keys():
            problems.append("Must have a 'derived_from' link to a " + \
                            "microb_assay_prep or a host_assay_prep.")

        self.logger.debug("Number of validation problems: %s.", len(problems))

        return problems

    def is_valid(self):
        """
        Validates the current object's data/JSON against the current schema
        in the OSDF instance for the specific object. However, unlike
        validates(), this method does not provide exact error messages,
        it states if the validation was successful or not.

        Args:
            None

        Returns:
            True if the data validates, False if the current state of
            fields in the instance do not validate with the OSDF instance
        """
        self.logger.debug("In is_valid.")

        problems = self.validate()

        valid = True
        if len(problems):
            self.logger.error("There were %s problems.", len(problems))
            valid = False

        self.logger.debug("Valid? %s", str(valid))

        return valid

    def _get_raw_doc(self):
        """
        Generates the raw JSON document for the current object. All required
        fields are filled into the JSON document, regardless of whether they
        were set or not. Any remaining fields are included only if they are
        set. This allows the user to visualize the JSON to ensure fields are set
        appropriately before saving into the database.

        Args:
            None

        Returns:
            An object representation of the JSON document.
        """
        self.logger.debug("In _get_raw_doc.")

        doc = {
            'acl': {
                'read': ['all'],
                'write': [ProteomeNonPride.namespace]
            },
            'linkage': self._links,
            'ns': ProteomeNonPride.namespace,
            'node_type': 'proteome_nonpride',
            'meta': {
                'comment': self._comment,
                'data_processing_protocol': self._data_processing_protocol,
                'other_url': self._other_url,
                'peak_url': self._peak_url,
                'processing_method': self._processing_method,
                'protmod_url': self._protmod_url,
                'raw_url': self._raw_url,
                'study': self._study,
                'subtype': self._subtype,
                'tags': self._tags
            }
        }

        if self._id is not None:
            self.logger.debug("Object has the OSDF id set.")
            doc['id'] = self._id

        if self._version is not None:
            self.logger.debug("Object has the OSDF version set.")
            doc['ver'] = self._version

        # Handle optional properties
        if self._analyzer is not None:
            self.logger.debug("Object has the 'analyzer' property set.")
            doc['meta']['analyzer'] = self._analyzer

        if self._date is not None:
            self.logger.debug("Object has the 'date' property set.")
            doc['meta']['date'] = self._date

        if self._detector is not None:
            self.logger.debug("Object has the 'detector' property set.")
            doc['meta']['detector'] = self._detector

        if self._exp_description is not None:
            self.logger.debug("Object has the 'exp_description' property set.")
            doc['meta']['exp_description'] = self._exp_description

        if self._instrument_name is not None:
            self.logger.debug("Object has the 'instrument_name' property set.")
            doc['meta']['instrument_name'] = self._instrument_name

        if self._private_files is not None:
            self.logger.debug("Object has the 'private_files' property set.")
            doc['meta']['private_files'] = self._private_files

        if self._protmod_format is not None:
            self.logger.debug("Object has the 'protmod_format' property set.")
            doc['meta']['protmod_format'] = self._protmod_format

        if self._protocol_name is not None:
            self.logger.debug("Object has the 'protocol_name' property set.")
            doc['meta']['protocol_name'] = self._protocol_name

        if self._protocol_steps is not None:
            self.logger.debug("Object has the 'protocol_steps' property set.")
            doc['meta']['protocol_steps'] = self._protocol_steps

        if self._reference is not None:
            self.logger.debug("Object has the 'reference' property set.")
            doc['meta']['reference'] = self._reference

        if self._search_engine is not None:
            self.logger.debug("Object has the 'search_engine' property set.")
            doc['meta']['search_engine'] = self._search_engine

        if self._short_label is not None:
            self.logger.debug("Object has the 'short_label' property set.")
            doc['meta']['short_label'] = self._short_label

        if self._software is not None:
            self.logger.debug("Object has the 'software' property set.")
            doc['meta']['software'] = self._software

        if self._source is not None:
            self.logger.debug("Object has the 'source' property set.")
            doc['meta']['source'] = self._source

        if self._title is not None:
            self.logger.debug("Object has the 'title' property set.")
            doc['meta']['title'] = self._title

        return doc

    @staticmethod
    def required_fields():
        """
        A static method. The required fields for the class.

        Args:
            None
        Returns:
            Tuple of strings of required properties.
        """
        module_logger.debug("In required_fields.")

        return ("local_other_file", "leak_peak_file", "local_protmod_file",
                "local_raw_file", "study", "subtype", "tags")

    def delete(self):
        """
        Deletes the current object (self) from OSDF. If the object has not been
        previously saved (node ID is not set), then an error message will be
        logged stating the object was not deleted. If the ID is set, and exists
        in the OSDF instance, then the object will be deleted from the OSDF
        instance, and this object must be re-saved in order to use it again.

        Args:
            None

        Returns:
            True upon successful deletion, False otherwise.
        """
        self.logger.debug("In delete.")

        if self._id is None:
            self.logger.warn("Attempt to delete a %s with no ID.", __name__)
            raise Exception("%s does not have an ID." % __name__)

        prot_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting %s with ID %s.", __name__, prot_id)
            session.get_osdf().delete_node(prot_id)
            success = True
        except Exception as delete_exception:
            self.logger.exception(delete_exception)
            self.logger.error("An error occurred when deleting %s.", self)

        return success

    @staticmethod
    def search(query="\"proteome_nonpride\"[node_type]"):
        """
        Searches OSDF for ProteomeNonPride nodes. Any criteria the user
        wishes to add is provided by the user in the query language
        specifications provided in the OSDF documentation. A general format
        is (including the quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as Cytokine instances,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         ProteomeNonPride node type.

        Returns:
            Returns an array of ProteomeNonPride objects. It returns an empty
            list if there are no results.
        """
        module_logger.debug("In search.")

        # Searching without any parameters will return all different results
        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"proteome_nonpride"[node_type]':
            query = '({}) && "proteome_nonpride"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: %s", query)

        prot_data = session.get_osdf().oql_query(ProteomeNonPride.namespace, query)

        all_results = prot_data['results']

        result_list = list()

        if len(all_results) > 0:
            for result in all_results:
                prot_result = ProteomeNonPride.load_proteome_nonpride(result)
                result_list.append(prot_result)

        return result_list

    @staticmethod
    def load_proteome_nonpride(prot_data):
        """
        Takes the provided JSON string and converts it to a
        ProteomeNonPride object

        Args:
            prot_data (str): The JSON string to convert

        Returns:
            Returns a ProteomeNonPride instance.
        """
        module_logger.info("Creating a template %s.", __name__)
        prot = ProteomeNonPride()

        module_logger.debug("Filling in %s details.", __name__)
        prot._set_id(prot_data['id'])
        prot.links = prot_data['linkage']
        prot.version = prot_data['ver']

        # Required fields
        prot.comment = prot_data['meta']['comment']
        prot.data_processing_protocol = prot_data['meta']['data_processing_protocol']
        prot.processing_method = prot_data['meta']['processing_method']
        prot.study = prot_data['meta']['study']
        prot.subtype = prot_data['meta']['subtype']
        prot.tags = prot_data['meta']['tags']
        # We need to use the private attributes here because there are no
        # public setters.
        prot._peak_url = prot_data['meta']['peak_url']
        prot._protmod_url = prot_data['meta']['protmod_url']
        prot._other_url = prot_data['meta']['other_url']
        prot._raw_url = prot_data['meta']['raw_url']

        # Optional fields
        if 'analyzer' in prot_data['meta']:
            prot.analyzer = prot_data['meta']['analyzer']

        if 'date' in prot_data['meta']:
            prot.date = prot_data['meta']['date']

        if 'detector' in prot_data['meta']:
            prot.detector = prot_data['meta']['detector']

        if 'exp_description' in prot_data['meta']:
            prot.exp_description = prot_data['meta']['exp_description']

        if 'instrument_name' in prot_data['meta']:
            prot.instrument_name = prot_data['meta']['instrument_name']

        if 'private_files' in prot_data['meta']:
            prot.private_files = prot_data['meta']['private_files']

        if 'protmod_format' in prot_data['meta']:
            prot.protmod_format = prot_data['meta']['protmod_format']

        if 'protocol_name' in prot_data['meta']:
            prot.protocol_name = prot_data['meta']['protocol_name']

        if 'protocol_steps' in prot_data['meta']:
            prot.protocol_steps = prot_data['meta']['protocol_steps']

        if 'reference' in prot_data['meta']:
            prot.reference = prot_data['meta']['reference']

        if 'search_engine' in prot_data['meta']:
            prot.search_engine = prot_data['meta']['search_engine']

        if 'short_label' in prot_data['meta']:
            prot.short_label = prot_data['meta']['short_label']

        if 'software' in prot_data['meta']:
            prot.software = prot_data['meta']['software']

        if 'source' in prot_data['meta']:
            prot.source = prot_data['meta']['source']

        if 'title' in prot_data['meta']:
            prot.title = prot_data['meta']['title']

        module_logger.debug("Returning loaded %s.", __name__)

        return prot

    @staticmethod
    def load(prot_id):
        """
        Loads the data for the specified input ID from the OSDF instance to
        this object.  If the provided ID does not exist, then an error message
        is provided stating the project does not exist.

        Args:
            prot_id (str): The OSDF ID for the document to load.

        Returns:
            A ProteomeNonPride object with all the available OSDF data loaded
            into it.
        """
        module_logger.debug("In load. Specified ID: %s", prot_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")
        prot_data = session.get_osdf().get_node(prot_id)
        prot = ProteomeNonPride.load_proteome_nonpride(prot_data)

        module_logger.debug("Returning loaded %s.", __name__)

        return prot

    def _upload_files(self, file_map):
        self.logger.debug("In _upload_files.")

        study2dir = {
            "ibd": "ibd",
            "preg_preterm": "ptb",
            "prediabetes": "t2d"
        }

        study = self.study
        subtype = self.subtype

        if study not in study2dir:
            raise ValueError("Invalid study. No directory mapping for %s" % study)

        study_dir = study2dir[study]
        remote_paths = {}

        # Get the session so we can get the username and password
        session = iHMPSession.get_session()
        username = session.username
        password = session.password

        # For each of the Proteome data files (there are 4), transmit them
        # to the Aspera server and return a dictionary with the computed remote
        # paths...
        for file_type, local_file in file_map.iteritems():
            self.logger.debug("Uploading %s of %s type %s",
                              __name__,
                              local_file,
                              file_type
                             )

            remote_base = os.path.basename(local_file)

            valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
            remote_base = ''.join(c for c in remote_base if c in valid_chars)
            remote_base = remote_base.replace(' ', '_') # No spaces in filenames

            remote_path = "/".join(["/" + study_dir, "proteome_nonpride",
                                    subtype, file_type, remote_base])
            self.logger.debug("Remote path for this file will be %s.", remote_path)

            # Upload the file to the iHMP aspera server
            upload_success = aspera.upload_file(ProteomeNonPride.aspera_server,
                                                username,
                                                password,
                                                local_file,
                                                remote_path)
            if not upload_success:
                self.logger.error(
                    "Experienced an error uploading file %s.", local_file)
                raise Exception("Unable to upload " + local_file)
            else:
                remote_paths[file_type] = "fasp://" + ProteomeNonPride.aspera_server + remote_path

        return remote_paths

    def save(self):
        """
        Saves the data in OSDF. The JSON form of the current data for the
        instance is first validated. If the data is not valid, then the data
        will not be saved. If the instance was saved previously, then the node
        ID is assigned the alphanumeric found in the OSDF instance. If not
        saved previously, then the node ID is 'None', and upon a successful
        save, will be assigned to the alphanumeric ID found in OSDF.

        Args:
            None

        Returns;
            True if successful, False otherwise.

        """
        self.logger.debug("In save.")

        # If node previously saved, use edit_node instead since ID
        # is given (an update in a way)
        # can also use get_node to check if the node already exists
        if not self.is_valid():
            self.logger.error("Cannot save, data is invalid.")
            return False

        session = iHMPSession.get_session()

        self.logger.info("Got iHMP session.")

        success = False

        if self._private_files:
            self._other_url = ["<private>"]
            self._peak_url = ["<private>"]
            self._protmod_url = ["<private>"]
            self._raw_url = ["<private>"]
        else:
            files = {
                "other": self._local_other_file,
                "peak": self._local_peak_file,
                "protmod": self._local_protmod_file,
                "raw": self._local_raw_file
            }

            remote_files = {}
            try:
                remote_files = self._upload_files(files)
            except Exception as upload_exception:
                self.logger.exception("Unable to transmit data via Aspera. Reason: %s.",
                                      upload_exception
                                     )
                return False

            self.logger.info("Aspera transmission of %s files successful.", __name__)

            self.logger.debug("Setting url properties with remote paths.")
            self._other_url = [remote_files['other']]
            self._peak_url = [remote_files['peak']]
            self._protmod_url = [remote_files['protmod']]
            self._raw_url = [remote_files['raw']]

        osdf = session.get_osdf()

        if self._id is None:
            # The document has not yet been saved
            self.logger.info("About to insert a new %s OSDF node.", __name__)

            # Get the JSON form of the data and load it
            self.logger.debug("Converting %s to parsed JSON form.", __name__)
            data = json.loads(self.to_json())
            self.logger.info("Got the raw JSON document.")

            try:
                self.logger.info("Attempting to save a new node.")
                node_id = osdf.insert_node(data)

                self._set_id(node_id)
                self._version = 1

                self.logger.info("Save for %s %s successful.", __name__, node_id)
                self.logger.info("Setting ID for %s %s.", __name__, node_id)

                success = True
            except Exception as save_exception:
                self.logger.exception(save_exception)
                self.logger.error("An error occurred while saving %s. " + \
                                  "Reason: %s", __name__, save_exception)
        else:
            self.logger.info("%s already has an ID, so we do an update " + \
                             "(not an insert).", __name__)

            try:
                prot_data = self._get_raw_doc()
                prot_id = self._id
                self.logger.info("Attempting to update %s with ID: %s.", __name__, prot_id)
                osdf.edit_node(prot_data)
                self.logger.info("Update for %s %s successful.", __name__, prot_id)

                prot_data = osdf.get_node(prot_id)
                latest_version = prot_data['ver']

                self.logger.debug("The version of this %s is now: %s",
                                  __name__, str(latest_version)
                                 )
                self._version = latest_version
                success = True
            except Exception as update_exception:
                self.logger.exception(update_exception)
                self.logger.error("An error occurred while updating %s %s. " + \
                                  "Reason: %s.", __name__,
                                  self._id,
                                  update_exception
                                 )

        self.logger.debug("Returning %s", str(success))

        return success
