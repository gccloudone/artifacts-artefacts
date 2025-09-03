# Frequently Asked Questions

**Question:** We want to limit people uploading things to Artifactory because we aren't confident that they will be able to tell the difference between something that is Unclassified, Protected A, or Protected B.
 
**Answer:** In Artifactory with Projects, you can control who can upload artifacts by combining Labels and Roles for fine-grained access control. Labels help classify repositories or artifacts (e.g., “Unclassified”, “Protected A”) and can be used to enforce policies or visibility. You can create Local Repositories only when necessary, and then use Project Roles to restrict upload (deploy) permissions to specific users or groups based on their role. Assign permissions at the project level and tie them to labels to ensure only authorized users can push to repositories labeled “Unclassified”. This way, even if a local repo exists, only vetted users can upload to it, aligning with your goal without broadly enabling uploads.

---

**Question:** With respect to my Departmental project space. I still have access to the "All Projects" option and it's showing all the Projects under Artifactory rather then just my own.

**Answer:** We have confirmed through JFrog that you should not have the ability to traverse into other projects. If you can please let us know and we can review the set of permissions granted.

---

**Question:** In the documentation around [permissions](https://jfrog.com/help/r/jfrog-platform-administration-documentation/create-and-manage-permissions) for JFrog, it highlights that we should be able to create permissions and assign them to Remote Repositories but I can't see this option in my Project Space.

**Answer:** At the global level in JFrog, you can create and manage permissions that apply to repositories, including Remote Repositories, as documented above. However, once you're inside a Project (or Space), access control is handled differently. Within a project, you define roles, and a Project Admin can create these roles and assign them to specific users or groups. These roles determine what actions users can perform within the project, including read, write, and manage permissions for specific repositories. Additionally, you can use Labels to classify repositories (e.g., “Unclassified”) and help enforce policy-based access, ensuring that only authorized users can interact with certain types of content. This model helps restrict uploads while still allowing flexibility when a need is validated.
