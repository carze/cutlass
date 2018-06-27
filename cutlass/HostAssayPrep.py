"""
Models the host assay prep object.
"""

import json
import logging
from itertools import count
from cutlass.iHMPSession import iHMPSession
from cutlass.Base import Base
from cutlass.Util import enforce_int, enforce_string

# pylint: disable=C0302, W0703

# Create a module logger named after the module
module_logger = logging.getLogger(__name__)
# Add a NullHandler for the case if no logging is configured by the application
module_logger.addHandler(logging.NullHandler())

class HostAssayPrep(Base):
    """
    The class encapsulates iHMP host assay prep data.  It contains all
    the fields required to save a such an object in OSDF.

    Attributes:
        namespace (str): The namespace this class will use in OSDF.
    """
    namespace = "ihmp"

    def __init__(self, *args, **kwargs):
        """
        Constructor for the HostAssayPrep class. This initializes the
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
        self._center = None
        self._comment = None
        self._contact = None
        self._experiment_type = None
        self._prep_id = None
        self._pride_id = None
        self._sample_name = None
        self._storage_duration = None
        self._study = None
        self._title = None

        # Optional properties
        self._cell_type = None
        self._exp_description = None
        self._protocol_name = None
        self._protocol_steps = None
        self._reference = None
        self._sample_description = None
        self._short_label = None
        self._species = None
        self._tissue = None
        self._urls = None

        super(HostAssayPrep, self).__init__(*args, **kwargs)

    @property
    def comment(self):
        """
        str: A descriptive comment for the prep.
        """
        self.logger.debug("In 'comment' getter.")

        return self._comment

    @comment.setter
    @enforce_string
    def comment(self, comment):
        """
        The setter for a descriptive comment for the prep object.

        Args:
            comment (str): The comment text.

        Returns:
            None
        """
        self.logger.debug("In 'comment' setter.")

        self._comment = comment

    @property
    def pride_id(self):
        """
        str: PRIDE identifier corresponding to study.
        """
        self.logger.debug("In 'pride_id' getter.")

        return self._pride_id

    @pride_id.setter
    @enforce_string
    def pride_id(self, pride_id):
        """
        The setter for the PRIDE identifier corresponding to study.

        Args:
            pride_id (str): The PRIDE identifier

        Returns:
            None
        """
        self.logger.debug("In 'pride_id' setter.")

        self._pride_id = pride_id

    @property
    def sample_name(self):
        """
        str: The short label that is referable to the sample used to
        generate the dataset.
        """
        self.logger.debug("In 'sample_name' getter.")

        return self._sample_name

    @sample_name.setter
    @enforce_string
    def sample_name(self, sample_name):
        """
        The setter for the short label that is referable to the sample
        used to generate the dataset.

        Args:
            sample_name (str): Short label for the sample.

        Returns:
            None
        """
        self.logger.debug("In 'sample_name' setter.")

        self._sample_name = sample_name

    @property
    def title(self):
        """
        str: The description of the particular experiment.
        """
        self.logger.debug("In 'title' getter.")

        return self._title

    @title.setter
    @enforce_string
    def title(self, title):
        """
        The setter for the description of the particular experiment.

        Args:
            title (str): Experiment title

        Returns:
            None
        """
        self.logger.debug("In 'title' setter.")

        self._title = title

    @property
    def short_label(self):
        """
        str: The short label/nomenclature used to group/organize experiments.
        """
        self.logger.debug("In 'short_label' getter.")

        return self._short_label

    @short_label.setter
    @enforce_string
    def short_label(self, short_label):
        """
        Set the short label/nomenclature used to group/organize experiments.

        Args:
            short_label (str): Short label used to group experiments

        Returns:
            None
        """
        self.logger.debug("In 'short_label' setter.")

        self._short_label = short_label

    @property
    def center(self):
        """
        str: The center responsible for generating the microbiome assay Prep.
        """
        self.logger.debug("In 'center' getter.")

        return self._center

    @center.setter
    @enforce_string
    def center(self, center):
        """
        Set the center responsible for generating the microbiome assay prep.

        Args:
            center (str): The center responsible for generating the
            microbiome assay prep.

        Returns:
            None
        """
        self.logger.debug("In 'center' setter.")

        self._center = center

    @property
    def contact(self):
        """
        str: Get the name and email of the primary contact at the center.
        """
        self.logger.debug("In 'contact' getter.")

        return self._contact

    @contact.setter
    @enforce_string
    def contact(self, contact):
        """
        Set the name and email of the primary contact at the center.

        Args:
            contact (str): Name and email of the primary contact at the center.

        Returns:
            None
        """
        self.logger.debug("In 'contact' setter.")

        self._contact = contact

    @property
    def prep_id(self):
        """
        str: Get the internal assay prep ID.
        """
        self.logger.debug("In 'prep_id' getter.")

        return self._prep_id

    @prep_id.setter
    @enforce_string
    def prep_id(self, prep_id):
        """
        Set the internal assay prep ID.

        Args:
            prep_id (str): Internal assay prep ID.

        Returns:
            None
        """
        self.logger.debug("In 'prep_id' setter.")

        self._prep_id = prep_id

    @property
    def storage_duration(self):
        """
        str: Get the MIGS/MIMS storage duration in days.
        """
        self.logger.debug("In 'storage_duration' getter.")

        return self._storage_duration

    @storage_duration.setter
    @enforce_int
    def storage_duration(self, storage_duration):
        """
        Set the MIGS/MIMS storage duration in days.

        Args:
            storage_duration (int): Storage duration in days.

        Returns:
            None
        """
        self.logger.debug("In 'storage_duration' setter.")

        self._storage_duration = storage_duration

    @property
    def experiment_type(self):
        """
        str: Get the PRIDE experiment type.
        """
        self.logger.debug("In 'experiment_type' getter.")

        return self._experiment_type

    @experiment_type.setter
    @enforce_string
    def experiment_type(self, experiment_type):
        """
        Set the PRIDE experiment type.

        Args:
            experiment_type (str): Experiment type, as defined by PRIDE.

        Returns:
            None
        """
        self.logger.debug("In 'experiment_type' setter.")

        self._experiment_type = experiment_type

    @property
    def species(self):
        """
        str: Controlled vocabulary term to describe a single species. NEWT CV
        terms are allowed.
        """
        self.logger.debug("In 'species' getter.")

        return self._species

    @species.setter
    @enforce_string
    def species(self, species):
        """
        Controlled vocabulary term to describe a single species. NEWT CV
        terms are allowed.

        Args:
            species (str): Term to describe a single species.

        Returns:
            None
        """
        self.logger.debug("In 'species' setter.")

        self._species = species

    @property
    def cell_type(self):
        """
        str: Controlled vocabulary term to describe a single cell type. Cell
        type ontology CV terms are allowed.
        """
        self.logger.debug("In 'cell_type' getter.")

        return self._cell_type

    @cell_type.setter
    @enforce_string
    def cell_type(self, cell_type):
        """
        Controlled vocabulary term to describe a single cell type. Cell
        type ontology CV terms are allowed.

        Args:
            cell_type (str): Term to describe the cell type.

        Returns:
            None
        """
        self.logger.debug("In 'cell_type' setter.")

        self._cell_type = cell_type

    @property
    def tissue(self):
        """
        str: Controlled vocabulary term to describe a single tissue. BRENDA
        Tissue CV terms are allowed.
        """
        self.logger.debug("In 'tissue' getter.")

        return self._tissue

    @tissue.setter
    @enforce_string
    def tissue(self, tissue):
        """
        Controlled vocabulary term to describe a single tissue. BRENDA Tissue
        CV terms are allowed.

        Args:
            tissue (str): Term to describe the tissue.

        Returns:
            None
        """
        self.logger.debug("In 'tissue' setter.")

        self._tissue = tissue

    @property
    def urls(self):
        """
        list: List of URL strings to relevant electronic resources.
        """
        self.logger.debug("In 'urls' getter.")

        return self._urls

    @urls.setter
    def urls(self, urls):
        """
        URLs of relevant electronic resources.

        Args:
            urls (list): List of URL strings

        Returns:
            None
        """

        self._urls = urls

    @property
    def reference(self):
        """
        str: Link to literature citation for which this experiment provides
        supporting evidence.
        """
        self.logger.debug("In 'reference' getter.")

        return self._reference

    @reference.setter
    @enforce_string
    def reference(self, reference):
        """
        Set the literature citation for which this experiment provides
        supporting evidence.

        Args:
            reference (str): Supporting evidence link.

        Returns:
            None
        """
        self.logger.debug("In 'reference' setter.")

        self._reference = reference

    @property
    def protocol_name(self):
        """
        str: The protocol title with versioning.
        """
        self.logger.debug("In 'protocol_name' getter.")

        return self._protocol_name

    @protocol_name.setter
    @enforce_string
    def protocol_name(self, protocol_name):
        """
        Set the protocol title with versioning.

        Args:
            protocol_name (str): Protocol title with versioning, ideally,
            pointing to a URL.

        Returns:
            None
        """
        self.logger.debug("In 'protocol_name' setter.")

        self._protocol_name = protocol_name

    @property
    def protocol_steps(self):
        """
        str: Description of the sample processing steps.
        """
        self.logger.debug("In 'protocol_steps' getter.")

        return self._protocol_steps

    @protocol_steps.setter
    @enforce_string
    def protocol_steps(self, protocol_steps):
        """
        Set the description of the sample processing steps.

        Args:
            protocol_name (str): Protocol title with versioning, ideally,
            pointing to a URL.

        Returns:
            None
        """
        self.logger.debug("In 'protocol_steps' setter.")

        self._protocol_steps = protocol_steps

    @property
    def exp_description(self):
        """
        str: Description of the goals and objectives of this study.
        """
        self.logger.debug("In 'exp_description' getter.")

        return self._exp_description

    @exp_description.setter
    @enforce_string
    def exp_description(self, exp_description):
        """
        Set the description of the goals and objectives of this study,
        summary of the abstract, optimally 2-3 sentences.

        Args:
            exp_description (str): Description of the goals/objectives
            of the study.

        Returns:
            None
        """
        self.logger.debug("In 'exp_description' setter.")

        self._exp_description = exp_description

    @property
    def sample_description(self):
        """
        str: Expansible description of the sample used to generate the
        dataset.
        """
        self.logger.debug("In 'sample_description' getter.")

        return self._sample_description

    @sample_description.setter
    @enforce_string
    def sample_description(self, sample_description):
        """
        Set the expansible description of the sample used to generate the
        dataset

        Args:
            sample_description (str): Expansible description of the sample
            used to generate the dataset

        Returns:
            None
        """
        self.logger.debug("In 'sample_description' setter.")

        self._sample_description = sample_description

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

        if 'prepared_from' not in self._links.keys():
            problems.append("Must have a 'prepared_from' link to a sample.")

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

        document = self._get_raw_doc()

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        (valid, _error_message) = session.get_osdf().validate_node(document)

        if 'prepared_from' not in self._links.keys():
            valid = False

        self.logger.debug("Valid? %s", str(valid))

        return valid

    def _get_raw_doc(self):
        """
        Generates the raw JSON document for the current object. All required
        fields are filled into the JSON document, regardless they are set or
        not. Any remaining fields are included only if they are set. This
        allows the user to visualize the JSON to ensure fields are set
        appropriately before saving into the database.

        Args:
            None

        Returns:
            An object representation of the JSON document.
        """
        self.logger.debug("In _get_raw_doc.")

        prep_doc = {
            'acl': {
                'read': ['all'],
                'write': [HostAssayPrep.namespace]
            },
            'linkage': self._links,
            'ns': HostAssayPrep.namespace,
            'node_type': 'host_assay_prep',
            'meta': {
                'comment': self._comment,
                'sample_name': self._sample_name,
                'title': self._title,
                'center': self._center,
                'contact': self._contact,
                'prep_id': self._prep_id,
                'experiment_type': self._experiment_type,
                'subtype': self._study,
                'study': self._study,
                'tags': self._tags
            }
        }

        if self._id is not None:
            self.logger.debug("%s object has the OSDF id set.", __name__)
            prep_doc['id'] = self._id

        if self._version is not None:
            self.logger.debug("%s object has the OSDF version set.", __name__)
            prep_doc['ver'] = self._version

        # Handle HostAssayPrep optional properties
        if self._short_label is not None:
            self.logger.debug("%s object has the 'short_label' property set.", __name__)
            prep_doc['meta']['short_label'] = self._short_label

        if self._urls is not None:
            self.logger.debug("%s object has the 'url' property set.", __name__)
            prep_doc['meta']['urls'] = self._urls

        if self._pride_id is not None:
            self.logger.debug("%s object has the 'pride_id' property set.", __name__)
            prep_doc['meta']['pride_id'] = self._pride_id

        if self._species is not None:
            self.logger.debug("%s object has the 'species' property set.", __name__)
            prep_doc['meta']['species'] = self._species

        if self._cell_type is not None:
            self.logger.debug("%s object has the 'cell_type' property set.", __name__)
            prep_doc['meta']['cell_type'] = self._cell_type

        if self._tissue is not None:
            self.logger.debug("%s object has the 'tissue' property set.", __name__)
            prep_doc['meta']['tissue'] = self._tissue

        if self._protocol_name is not None:
            self.logger.debug("%s object has the 'protocol_name' property set.", __name__)
            prep_doc['meta']['protocol_name'] = self._protocol_name

        if self._protocol_steps is not None:
            self.logger.debug("%s object has the 'protocol_steps' property set.", __name__)
            prep_doc['meta']['protocol_steps'] = self._protocol_steps

        if self._reference is not None:
            self.logger.debug("%s object has the 'reference' property set.", __name__)
            prep_doc['meta']['reference'] = self._reference

        if self._exp_description is not None:
            self.logger.debug("%s object has the 'exp_description' property set.", __name__)
            prep_doc['meta']['exp_description'] = self._exp_description

        if self._sample_description is not None:
            self.logger.debug("%s object has the 'sample_description' property set.", __name__)
            prep_doc['meta']['sample_description'] = self._sample_description

        if self._storage_duration is not None:
            self.logger.debug("%s object has the 'storage_duration' property set.", __name__)
            prep_doc['meta']['storage_duration'] = self._storage_duration

        return prep_doc

    @staticmethod
    def required_fields():
        """
        A static method. The required fields for the class.

        Args:
            None
        Returns:
            Tuple of strings for required properties.
        """
        module_logger.debug("In required fields.")
        return ("comment", "sample_name", "title", "center", "contact",
                "prep_id", "experiment_type", "study", "tags")

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

        host_prep_id = self._id

        session = iHMPSession.get_session()
        self.logger.info("Got iHMP session.")

        # Assume failure
        success = False

        try:
            self.logger.info("Deleting %s with ID %s.", __name__, host_prep_id)
            session.get_osdf().delete_node(host_prep_id)
            success = True
        except Exception as delete_exception:
            self.logger.exception(delete_exception)
            self.logger.error("An error occurred when deleting %s.", self)

        return success

    @staticmethod
    def search(query="\"host_assay_prep\"[node_type]"):
        """
        Searches OSDF for HostAssayPrep nodes. Any criteria the user wishes to
        add is provided by the user in the query language specifications
        provided in the OSDF documentation. A general format is (including the
        quotes and brackets):

        "search criteria"[field to search]

        If there are any results, they are returned as HostAssayPrep instances,
        otherwise an empty list will be returned.

        Args:
            query (str): The query for the OSDF framework. Defaults to the
                         HostAssayPrep node type.

        Returns:
            Returns an array of HostAssayPrep objects. It returns an empty list
            if there are no results.
        """
        module_logger.debug("In search.")

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")

        if query != '"host_assay_prep"[node_type]':
            query = '({}) && "host_assay_prep"[node_type]'.format(query)

        module_logger.debug("Submitting OQL query: %s", query)

        prep_data = session.get_osdf().oql_query(HostAssayPrep.namespace, query)

        all_results = prep_data['results']

        result_list = list()

        if len(all_results) > 0:
            for result in all_results:
                prep_result = HostAssayPrep.load_host_assay_prep(result)
                result_list.append(prep_result)

        return result_list

    @staticmethod
    def load_host_assay_prep(prep_data):
        """
        Takes the provided JSON string and converts it to a
        HostAssayPrep object

        Args:
            prep_data (str): The JSON string to convert

        Returns:
            Returns a HostAssayPrep instance.
        """
        module_logger.info("Creating a template %s.", __name__)
        prep = HostAssayPrep()

        module_logger.debug("Filling in %s details.", __name__)
        prep._set_id(prep_data['id'])
        prep.links = prep_data['linkage']
        prep.version = prep_data['ver']

        # Required fields
        prep.comment = prep_data['meta']['comment']
        prep.contact = prep_data['meta']['contact']
        prep.center = prep_data['meta']['center']
        prep.experiment_type = prep_data['meta']['experiment_type']
        prep.prep_id = prep_data['meta']['prep_id']
        prep.sample_name = prep_data['meta']['sample_name']
        prep.study = prep_data['meta']['study']
        prep.tags = prep_data['meta']['tags']
        prep.title = prep_data['meta']['title']

        # Optional fields
        if 'short_label' in prep_data['meta']:
            prep.short_label = prep_data['meta']['short_label']

        if 'urls' in prep_data['meta']:
            prep.urls = prep_data['meta']['urls']

        if 'pride_id' in prep_data['meta']:
            prep.pride_id = prep_data['meta']['pride_id']

        if 'species' in prep_data['meta']:
            prep.species = prep_data['meta']['species']

        if 'cell_type' in prep_data['meta']:
            prep.cell_type = prep_data['meta']['cell_type']

        if 'tissue' in prep_data['meta']:
            prep.tissue = prep_data['meta']['tissue']

        if 'reference' in prep_data['meta']:
            prep.reference = prep_data['meta']['reference']

        if 'protocol_name' in prep_data['meta']:
            prep.protocol_name = prep_data['meta']['protocol_name']

        if 'protocol_steps' in prep_data['meta']:
            prep.protocol_steps = prep_data['meta']['protocol_steps']

        if 'exp_description' in prep_data['meta']:
            prep.exp_description = prep_data['meta']['exp_description']

        if 'sample_description' in prep_data['meta']:
            prep.sample_description = prep_data['meta']['sample_description']

        if 'storage_duration' in prep_data['meta']:
            prep.storage_duration = prep_data['meta']['storage_duration']

        module_logger.debug("Returning loaded %s.", __name__)
        return prep

    @staticmethod
    def load(prep_id):
        """
        Loads the data for the specified input ID from the OSDF instance to
        this object.  If the provided ID does not exist, then an error message
        is provided stating the project does not exist.

        Args:
            prep_id (str): The OSDF ID for the document to load.

        Returns:
            A HostAssayPrep object with all the available OSDF data loaded
            into it.
        """
        module_logger.debug("In load. Specified ID: %s", prep_id)

        session = iHMPSession.get_session()
        module_logger.info("Got iHMP session.")
        prep_data = session.get_osdf().get_node(prep_id)
        prep = HostAssayPrep.load_host_assay_prep(prep_data)

        module_logger.debug("Returning loaded %s.", __name__)

        return prep

    def save(self):
        """
        Saves the data in OSDF. The JSON form of the current data for the
        instance is validated in the save function. If the data is not valid,
        then the data will not be saved. If the instance was saved previously,
        then the node ID is assigned the alpha numeric found in the OSDF
        instance. If not saved previously, then the node ID is 'None', and upon
        a successful, will be assigned to the alpha numeric ID found in OSDF.
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

        osdf = session.get_osdf()

        success = False

        if self._id is None:
            self.logger.info("About to insert a new %s OSDF node.", __name__)

            # Get the JSON form of the data and load it
            self.logger.debug("Converting %s to parsed JSON form.", __name__)
            data = json.loads(self.to_json())

            try:
                node_id = osdf.insert_node(data)

                self._set_id(node_id)
                self._version = 1
                success = True
            except Exception as save_exception:
                self.logger.exception(save_exception)
                self.logger.error("An error occurred when saving %s.", self)
        else:
            self.logger.info("%s already has an ID, so we do an update (not an insert).",
                             __name__)

            try:
                prep_data = self._get_raw_doc()
                self.logger.info("%s already has an ID, so we do an update (not an insert).",
                                 __name__
                                )
                prep_id = self._id
                self.logger.debug("%s OSDF ID to update: %s.", __name__, prep_id)
                osdf.edit_node(prep_data)

                prep_data = osdf.get_node(prep_id)
                latest_version = prep_data['ver']

                self.logger.debug("The version of this %s is now: %s",
                                  __name__,
                                  str(latest_version)
                                 )
                self._version = latest_version
                success = True
            except Exception as update_exception:
                self.logger.exception(update_exception)
                self.logger.error("An error occurred when updating %s.", self)

        return success

    def cytokines(self):
        """
        Returns an iterator of all Cytokines connected to this HostAssayPrep.
        """
        self.logger.debug("In cytokines().")

        linkage_query = '"{}"[linkage.derived_from] and "cytokine"[node_type]'.format(self.id)

        query = iHMPSession.get_session().get_osdf().oql_query

        from cutlass.Cytokine import Cytokine

        for page_no in count(1):
            res = query(HostAssayPrep.namespace, linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield Cytokine.load_cytokine(doc)

            res_count -= len(res['results'])

            if res_count < 1:
                break

    def lipidomes(self):
        """
        Returns an iterator of all Lipidomes connected to this HostAssayPrep.
        """
        self.logger.debug("In lipidomes().")

        linkage_query = '"{}"[linkage.derived_from] and "lipidome"[node_type]'.format(self.id)

        query = iHMPSession.get_session().get_osdf().oql_query

        from cutlass.Lipidome import Lipidome

        for page_no in count(1):
            res = query(HostAssayPrep.namespace, linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield Lipidome.load_lipidome(doc)

            res_count -= len(res['results'])

            if res_count < 1:
                break

    def metabolomes(self):
        """
        Returns an iterator of all Metabolomes connected to this HostAssayPrep.
        """
        self.logger.debug("In metabolomes().")

        linkage_query = '"{}"[linkage.derived_from] and "metabolome"[node_type]'.format(self.id)

        query = iHMPSession.get_session().get_osdf().oql_query

        from cutlass.Metabolome import Metabolome

        for page_no in count(1):
            res = query(HostAssayPrep.namespace, linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield Metabolome.load_metabolome(doc)

            res_count -= len(res['results'])

            if res_count < 1:
                break

    def proteomes(self):
        """
        Returns an iterator of all Proteomes connected to this HostAssayPrep.
        """
        self.logger.debug("In proteomes().")

        linkage_query = '"{}"[linkage.derived_from] and "proteome"[node_type]'.format(self.id)

        query = iHMPSession.get_session().get_osdf().oql_query

        from cutlass.Proteome import Proteome

        for page_no in count(1):
            res = query(HostAssayPrep.namespace, linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield Proteome.load_proteome(doc)

            res_count -= len(res['results'])

            if res_count < 1:
                break

    def _derived_docs(self):
        self.logger.debug("In _derived_docs().")

        linkage_query = '"{}"[linkage.derived_from]'.format(self.id)
        query = iHMPSession.get_session().get_osdf().oql_query

        for page_no in count(1):
            res = query(HostAssayPrep.namespace, linkage_query, page=page_no)
            res_count = res['result_count']

            for doc in res['results']:
                yield doc
            res_count -= len(res['results'])

            if res_count < 1:
                break

    def derivations(self):
        """
        Return an iterator of all the derived nodes from this prep, including
        lipidomes, metabolomes, cytokines, etc...
        """
        self.logger.debug("In derivations().")

        from cutlass.Cytokine import Cytokine
        from cutlass.Lipidome import Lipidome
        from cutlass.Metabolome import Metabolome
        from cutlass.Proteome import Proteome
        from cutlass.Serology import Serology

        for doc in self._derived_docs():
            if doc['node_type'] == "lipidome":
                yield Lipidome.load_lipidome(doc)
            elif doc['node_type'] == "metabolome":
                yield Metabolome.load_metabolome(doc)
            elif doc['node_type'] == "cytokine":
                yield Cytokine.load_cytokine(doc)
            elif doc['node_type'] == "proteome":
                yield Proteome.load_proteome(doc)
            elif doc['node_type'] == "serology":
                yield Serology.load_serology(doc)
