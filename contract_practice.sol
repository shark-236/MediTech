{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00b80404-7438-4f72-aa04-0094bf4a42b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "// SPDX-License-Identifier: UNLICENSED\n",
    "\n",
    "pragma solidity ^0.5.0;\n",
    "\n",
    "contract TrialLog {\n",
    "    uint DateOfEntry;\n",
    "    string UserID = \"UserID\";\n",
    "    string group = \"Control or Test\";\n",
    "    uint DOB;\n",
    "    string sex = \"M or F\";\n",
    "    bool Consent;\n",
    "    uint ZipCode;\n",
    "    string ClinicIdentifier = \"Clinic Identifier\";\n",
    "    uint TrialPhase;\n",
    "    uint BloodPressure;\n",
    "    uint BodyTemp;\n",
    "    bool Fasting;\n",
    "    string MedAdministered = \"Medication Administered\";\n",
    "    bool HasSymptoms;\n",
    "    string result = \"Result\";\n",
    "\n",
    "\n",
    "    function updateLog(uint newDateOfEntry, string memory newUserID, string memory newgroup, uint newDOB, string memory newsex, bool newConsent, uint newZipCode, string memory NewClinicIdentifier, uint newTrialPhase, uint newBloodPressure, uint newBodyTemp, bool newFasting, string memory newMedAdministered, bool newHasSymptoms, string memory newresult) public {\n",
    "       DateOfEntry = newDateOfEntry;\n",
    "       UserID = newUserID;\n",
    "       group = newgroup;\n",
    "       DOB = newDOB;\n",
    "       sex = newsex;\n",
    "       Consent = newConsent; // Did they fulfill the consent agreement Y/N?\n",
    "       ZipCode = newZipCode;\n",
    "       ClinicIdentifier = NewClinicIdentifier;\n",
    "       TrialPhase = newTrialPhase;\n",
    "       BloodPressure = newBloodPressure;\n",
    "       BodyTemp = newBodyTemp;\n",
    "       Fasting = newFasting;\n",
    "       MedAdministered = newMedAdministered;\n",
    "       HasSymptoms = newHasSymptoms;\n",
    "       result = newresult;\n",
    "   }\n",
    "}"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "dev",
   "language": "python",
   "name": "dev"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
