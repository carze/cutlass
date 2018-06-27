"""
Models the annotation object.
"""

import json
import logging
import os
import string
from itertools import count
from cutlass.iHMPSession import iHMPSession
from cutlass.Base import Base
from cutlass.aspera import aspera
from cutlass.Util import *

# pylint: disable=W0703, C1801

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class Annotation(Base):
    """
    The class encapsulates iHMP annotation data. It contains all
    the fields required to save a such an object in OSDF.

    Attributes:
        date_format (str): The format of the date the annotation was made.

        namespace (str): The namespace this class will use in OSDF.
    """
    namespace = "ihmp"

    aspera_server = "aspera2.ihmpdcc.org"

    date_format = '%Y-%m-%d'

    def __init__(self, *args, **kwargs):
        """
        Constructor for the Annotation class. This initializes the
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
        self._annotation_pipeline = None
        self._checksums = {}
        self._format = None
        self._format_doc = None
        self._local_file = None
        self._orf_process = None
        self._size = None
        self._study = None
        self._urls = ['']

        # Optional properties
        self._comment = None
        self._date = None
        self._sop = None
        self._annotation_source = None
        self._private_files = None

        super(Annotation, self).__init__(*args, **kwargs)

    @property
    def annotation_pipeline(self):
        """
        str: Get the software and version used to generate the annotation.
        """
        self.logger.debug("In 'annotation_pipeline' getter.")

        return self._annotation_pipeline

    @annotation_pipeline.setter
    @enforce_string
    def annotation_pipeline(self, annotation_pipeline):
        """
        Set The software and version used to generate annotation.

        Args:
            annotation_pipeline (str): The software and version used to
            generate annotation.

        Returns:
            None
        """
        self.logger.debug("In 'annotation_pipeline' setter.")

        self._annotation_pipeline = annotation_pipeline

    @property
    def annotation_source(self):
        """
        str: Get the databases used for providing curation.
        """
        self.logger.debug("In 'annotation_source' getter.")

        return self._annotation_source

    @annotation_source.setter
    @enforce_string
    def annotation_source(self, annotation_source):
        """
        Set the databases used for providing curation; or for cases where
        annotation was provided by a community jamboree or model organism
        database.

        Args:
            annotation_source (str): The databases used for providing
            curation.

        Returns:
            None
        """
        self.logger.debug("In 'annotation_source' setter.")

        self._annotation_source = annotation_source

    @property
    def checksums(self):
        """
        dict: The annotation's checksum data.
        """
        self.logger.debug("In checksums getter.")
        return self._checksums

    @checksums.setter
    @enforce_dict
    def checksums(self, checksums):
        """
        The setter for the Annotation's checksums.

        Args:
            checksums (dict): The checksums.

        Returns:
            None
        """
        self.logger.debug("In 'checksums' setter.")

        self._checksums = checksums

    @property
    def comment(self):
        """
        str: A descriptive comment for the annotation.
        """
        self.logger.debug("In 'comment' getter.")
        return self._comment

    @comment.setter
    @enforce_string
    def comment(self, comment):
        """
        The setter for a descriptive comment for the annotation.

        Args:
            comment (str): The comment text.

        Returns:
            None
        """
        self.logger.debug("In comment setter.")

        self._comment = comment

    @property
    def date(self):
        """
        str: The date on which the annotations were generated.
        """
        self.logger.debug("In 'date' getter.")

        return self._date

    @date.setter
    @enforce_string
    @enforce_past_date
    def date(self, date):
        """
        The setter the date of the annotation.

        Args:
            date (str): The date in YYYY-MM-DD format.

        Returns:
            None
        """
        self.logger.debug("In 'date' setter.")

        self._date = date

    @property
    def format(self):
        """
        str: The file format of the annotation file.
        """
        self.logger.debug("In 'format' getter.")

        return self._format

    @format.setter
    @enforce_string
    def format(self, format):
        """
        The setter for the file format of the annotation file.

        Args:
            format (str): The file format of the annotation file.

        Returns:
            None
        """
        self.logger.debug("In 'format' setter.")

        self._format = format

    @property
    def format_doc(self):
        """
        str: URL for documentation of file format.
        """
        self.logger.debug("In format_doc getter.")
        return self._format_doc

    @format_doc.setter
    @enforce_string
    def format_doc(self, format_doc):
        """
        The setter for the URL for the documentation of the file format.

        Args:
            format_doc (str): URL for file format documentation.

        Returns:
            None
        """
        self.logger.debug("In 'format_doc' setter.")

        self._format_doc = format_doc

    @property
    def orf_process(self):
        """
        str: The software and version used to generate gene predictions.
        """
        self.logger.debug("In 'orf_process' getter.")

        return self._orf_process

    @orf_process.setter
    @enforce_string
    def orf_process(self, orf_process):
        """
        Set the software and version used to generate gene predictions.

        Args:
            orf_process (str): The software and version used.

        Returns:
            None
        """
        self.logger.debug("In 'orf_process' setter.")

        self._orf_process = orf_process

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
    def sop(self):
        """
        str: The URL for documentation of procedures used in annotation.
        """
        self.logger.debug("In 'sop' getter.")

        return self._sop

    @sop.setter
    @enforce_string
    def sop(self, sop):
        """
        Set the URL for documentation of procedures used in annotation.

        Args:
            sop (str): The documentation URL.

        Returns:
            None
        """
        self.logger.debug("In 'sop' setter.")

        self._sop = sop

    @property
    def size(self):
        """
        int: The size of the file in bytes.
        """
        self.logger.debug("In 'size' getter.")

        return self._size

    @size.setter
    @enforce_int
    def size(self, size):
        """
        The setter for the file size.

        Args:
            size (int): The size of the file in bytes.

        Returns:
            None
        """
        self.logger.debug("In 'size' setter.")

        if size < 0:
            raise ValueError("The size must be non-negative.")

        self._size = size

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

        self._study = study

    @property
    def local_file(self):
        """
        str: Path to the local file to upload to the server.
        """
        self.logger.debug("In 'local_file' getter.")

        return self._local_file

    @local_file.setter
    @enforce_string
    def local_file(self, local_file):
        """
        The setter for the Annotation local file.

        Args:
            local_file (str): The path to the local file that should be uploaded
            to the server.

        Returns:
            None
        """
        self.logger.debug("In 'local_file' setter.")

        self._local_file = local_file

    @property
    def urls(self):
        """
        array: An array of string URLs from where the file can be obtained,
               http, ftp, fasp, etc...
        """
        self.logger.debug("In 'urls' getter.")

        return self._urls

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
            self.logger.info("Data is NOT private, so check that local_file is set.")
            if self._local_file is None:
                problems.append("Local file is not yet set.")
            elif not os.path.isfile(self._local_file):
                problems.append("Local file does not point to an actual file.")

        if 'computed_from' not in self._links.keys():
            problems.append("Must have a 'computed_from' link.")

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
            self.logger.error("There were %s problems.", str(len(problems)))
            valid = False

        self.logger.debug("Valid? %s", str(valid))

        return valid

    def _get_raw_doc(self):
        """
        Generates the raw JSON document for the current object. All required
        fields are filled in, regardless of whether they are set or not. Any
        remaining fields are included only if they are set.

        Args:
            None

        Returns:
            An object representation of the JSON document.
        """
        self.logger.debug("In _get_raw_doc.")

        doc = {
            'acl': {
                'read': ['all'],
                'write': [Annotation.namespace]
            },
            'linkage': self._links,
            'ns': Annotation.namespace,
            'node_type': 'annotation',
            'meta': {
                'annotation_pipeline': self._annotation_pipeline,
                'checksums': self._checksums,
                'format': self._format,
                'format_doc': self._format_doc,
                'orf_process': self._orf_process,
                'size': self._size,
                'study': self._study,
                'subtype': self._study,
                'tags': self._tags,
                'urls': self._urls
            }
        }

        if self._id is not None:
            self.logger.debug("Object has the OSDF id set.")
            doc['id'] = self._id

        if self._version is not None:
            self.logger.debug("Object has the OSDF version set.")
            doc['ver'] = self._version

        # Handle optional properties
        if self._comment is not None:
            self.logger.debug("Object has the 'comment' property set.")
            doc['meta']['comment'] = self._comment

        if self._date is not None:
            self.logger.debug("Object has the 'date' property set.")
            doc['meta']['date'] = self._date

        if self._sop is not None:
            self.logger.debug("Object has the 'sop' property set.")
            doc['meta']['sop'] = self._sop

        if self._annotation_source is not None:
            self.logger.debug("Object has the 'annotation_source' property set.")
            doc['meta']['annotation_source'] = self._annotation_source

        if self._private_files is not None:
            self.logger.debug("Object has the 'private_files' property set.")
            doc['meta']['private_files'] = self._private_files

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
        module_logger.debug("In required fields.")
        return ("annotation_pipeline", "checksums", "format", "format_doc",
                "orf_process", "size", "study", "tags")

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
            self.logger.warn("Attempt to delete a Annotation with no ID.")
            raise Exception("Annotation does not have an ID.")

        annotation_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting Annotation with ID %s.", annotation_id)
            session.get_osdf().delete_node(annotation_id)
            success = True
        except Exception as e:
            self.logger.exception(e)
            self.logger.error("An error occurred when deleting %s.", self)

        return success

    @staticmethod
    def search(query="\"annotation\"[node_type]"):
        """
        Searches OSDF for Annotation nodes. Any criteria the user wishes to
        add is provided by the user in the query language specifications
        provided in the OSDF documentation. A general format is (including the
        quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as Annotation instances,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         Annotation node type.

        Returns:
            Returns an array of Annotation objects. It returns an empty list
            if there are no results.
        """
        module_logger.debug("In search.")

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"annotation"[node_type]':
            query = '({}) && "annotation"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: %s", query)

        annot_data = session.get_osdf().oql_query(Annotation.namespace, query)

        all_results = annot_data['results']

        result_list = list()

        if len(all_results) > 0:
            for result in all_results:
                annot_result = Annotation.load_annotation(result)
                result_list.append(annot_result)

        return result_list

    @staticmethod
    def load_annotation(annot_data):
        """
        Takes the provided JSON string and converts it to a
        Annotation object

        Args:
            annot_data (str): The JSON string to convert

        Returns:
            Returns a Annotation instance.
        """
        module_logger.info("Creating a template Annotation.")
        annot = Annotation()

        module_logger.debug("Filling in Annotation details.")

        # The attributes commmon to all iHMP nodes
        annot._set_id(annot_data['id'])
        annot.links = annot_data['linkage']
        annot.version = annot_data['ver']

        # Required fields
        annot.annotation_pipeline = annot_data['meta']['annotation_pipeline']
        annot.checksums = annot_data['meta']['checksums']
        annot.format = annot_data['meta']['format']
        annot.format_doc = annot_data['meta']['format_doc']
        annot.study = annot_data['meta']['study']
        annot.tags = annot_data['meta']['tags']
        # We need to use the private attribute here because there is no
        # public setter.
        annot._urls = annot_data['meta']['urls']

        # Optional fields
        if 'comment' in annot_data['meta']:
            annot.comment = annot_data['meta']['comment']

        if 'date' in annot_data['meta']:
            annot.date = annot_data['meta']['date']

        if 'sop' in annot_data['meta']:
            annot.sop = annot_data['meta']['sop']

        if 'annotation_source' in annot_data['meta']:
            annot.annotation_source = annot_data['meta']['annotation_source']

        if 'private_files' in annot_data['meta']:
            annot.private_files = annot_data['meta']['private_files']

        module_logger.debug("Returning loaded %s.", __name__)
        return annot

    @staticmethod
    def load(annot_id):
        """
        Loads the data for the specified input ID from the OSDF instance to
        this object.  If the provided ID does not exist, then an error message
        is provided stating the project does not exist.

        Args:
            annot_id (str): The OSDF ID for the document to load.

        Returns:
            A Annotation object with all the available OSDF data loaded
            into it.
        """
        module_logger.debug("In load. Specified ID: %s", annot_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")
        annot_data = session.get_osdf().get_node(annot_id)
        annot = Annotation.load_annotation(annot_data)

        module_logger.debug("Returning loaded Annotation.")

        return annot

    def _upload_data(self):
        self.logger.debug("In _upload_data.")

        session = iHMPSession.get_session()
        study = self._study

        study2dir = {
            "ibd": "ibd",
            "preg_preterm": "ptb",
            "prediabetes": "t2d"
        }

        if study not in study2dir:
            raise ValueError("Invalid study. No directory mapping for %s" % study)

        study_dir = study2dir[study]

        remote_base = os.path.basename(self._local_file)

        valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
        remote_base = ''.join(c for c in remote_base if c in valid_chars)
        remote_base = remote_base.replace(' ', '_') # No spaces in filenames

        remote_path = "/".join(["/" + study_dir, "genome", "microbiome", "wgs",
                                "analysis", "hmgi", remote_base])
        self.logger.debug("Remote path for this file will be %s.", remote_path)

        # Upload the file to the iHMP aspera server
        upload_result = aspera.upload_file(Annotation.aspera_server,
                                           session.username,
                                           session.password,
                                           self._local_file,
                                           remote_path)

        if not upload_result:
            self.logger.error("Experienced an error uploading the annotation. " + \
                              "Aborting save.")
            raise Exception("Unable to upload annotation.")
        else:
            self._urls = ["fasp://" + Annotation.aspera_server + remote_path]

    def save(self):
        """
        Saves the data in OSDF. The JSON form of the current data for the
        instance is validated in the save function. If the data is not valid,
        then the data will not be saved. If the instance was saved previously,
        then the node ID is assigned the alpha numeric found in the OSDF
        instance. If not saved previously, then the node ID is 'None', and upon
        a successful save, will be assigned the ID found in OSDF.
        Also, the version is updated as the data is saved in OSDF.

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
            self._urls = ["<private>"]
        else:
            try:
                self._upload_data()
            except Exception as e:
                self.logger.exception(e)
                # Don't bother continuing...
                return False

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

                self.logger.info("Save for " + __name__ + " %s successful." % node_id)
                self.logger.info("Setting ID for " + __name__ + " %s." % node_id)

                success = True
            except Exception as save_exception:
                self.logger.exception(save_exception)
                self.logger.error("An error occurred while saving %s. " + \
                                  "Reason: %s", __name__, save_exception)
        else:
            self.logger.info("%s already has an ID, so we do an update (not an insert).", __name__)

            try:
                annot_data = self._get_raw_doc()
                annot_id = self._id
                self.logger.info("Attempting to update %s with ID: %s.", __name__, annot_id)
                osdf.edit_node(annot_data)
                self.logger.info("Update for %s %s successful.", __name__, annot_id)

                annot_data = osdf.get_node(annot_id)
                latest_version = annot_data['ver']

                self.logger.debug("The version of this %s is now: %s",
                                  __name__,
                                  str(latest_version)
                                 )
                self._version = latest_version
                success = True
            except Exception as update_exception:
                self.logger.exception(update_exception)
                self.logger.error("An error occurred while updating " + \
                                  "%s %s. Reason: %s.", __name__, self._id, update_exception)

        self.logger.debug("Returning " + str(success))
        return success

    def clustered_seq_sets(self):
        """
        Returns an iterator of all ClusteredSeqSets connected to this Annotation.
        """
        self.logger.debug("In clustered_seq_sets.")

        linkage_query = '"{}"[linkage.computed_from]'.format(self.id)

        query = iHMPSession.get_session().get_osdf().oql_query

        from cutlass.ClusteredSeqSet import ClusteredSeqSet

        for page_no in count(1):
            res = query(Annotation.namespace, linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield ClusteredSeqSet.load_clustered_seq_set(doc)

            res_count -= len(res['results'])

            if res_count < 1:
                break
